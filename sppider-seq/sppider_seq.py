import os
import re
import random
from io import StringIO
from itertools import product
from datetime import datetime
import time
import urllib.request

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from Bio import SeqIO
from scipy.stats import norm
from statsmodels.stats.multitest import fdrcorrection
from transformers import EsmTokenizer, EsmModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ESM_MODEL_NAME = "facebook/esm2_t33_650M_UR50D"

tokenizer = None
esm_model = None

def ensure_esm_loaded():
    global tokenizer, esm_model
    if tokenizer is None or esm_model is None:
        tokenizer = EsmTokenizer.from_pretrained(ESM_MODEL_NAME)
        esm_model = EsmModel.from_pretrained(ESM_MODEL_NAME).to(device)
        for p in esm_model.parameters():
            p.requires_grad = False
        esm_model.eval()

EMBED_DIM = 1280
NUM_HEADS = 16
MAX_TOKENS = 1024
STRIDE = 512
PRED_CUTOFF = 0.50
PEPTIDE_MODEL_PATH = "/opt/SPPIDER-seq/models/crossattn_pep_run07_best.pt"
RECEPTOR_MODEL_PATH = "/opt/SPPIDER-seq/models/crossattn_rec_run27_best.pt"

embedding_cache = {}
EMBEDDING_CACHE_MAX_SEQS = 256
EMBEDDING_CACHE_MAX_LEN = 3000

def get_or_compute_embeddings(sequence, allow_cache=True):
    seq = sequence.strip()
    if not seq:
        return [], 0
    seq_key = seq.upper()
    if allow_cache and seq_key in embedding_cache:
        return embedding_cache[seq_key]
    chunk_dicts, L = embed_sequence_chunks(seq)
    if allow_cache and L <= EMBEDDING_CACHE_MAX_LEN and len(embedding_cache) < EMBEDDING_CACHE_MAX_SEQS:
        embedding_cache[seq_key] = (chunk_dicts, L)
    return chunk_dicts, L

def sanitize_filename(text):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', text)

def parse_fasta(text):
    records = list(SeqIO.parse(StringIO(text.strip()), "fasta"))
    return [(i, rec.id, str(rec.seq)) for i, rec in enumerate(records)]

def scramble_sequence(seq, seed=None):
    rng = random.Random(seed)
    arr = list(seq)
    rng.shuffle(arr)
    return ''.join(arr)

def embed_sequence_chunks(sequence, max_tokens=MAX_TOKENS, stride=STRIDE):
    ensure_esm_loaded()
    esm_model.eval()
    device_local = next(esm_model.parameters()).device
    win = max_tokens - 2
    L = len(sequence)
    if L == 0:
        return [], 0
    chunk_data = []
    for start in range(0, L, stride):
        end = min(start + win, L)
        if end <= start:
            break
        enc = tokenizer(sequence[start:end],
                        return_tensors="pt",
                        add_special_tokens=True)
        input_ids = enc["input_ids"].to(device_local)
        with torch.no_grad():
            out = esm_model(input_ids)
            emb = out.last_hidden_state[:, 1:-1, :].squeeze(0).contiguous()
        chunk_data.append({
            "start_idx": start,
            "end_idx": end,
            "embedding": emb.cpu()
        })
        if end == L:
            break
    return chunk_data, L

class CrossAttentionLayer(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.cross_attn = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, query, context, context_mask=None):
        out, _ = self.cross_attn(query, context, context, key_padding_mask=context_mask)
        return self.norm(query + out)

class ChunkwiseInteractionModel(nn.Module):
    def __init__(self, embed_dim=EMBED_DIM, num_heads=NUM_HEADS, initial_bias=None):
        super().__init__()
        self.cross = CrossAttentionLayer(embed_dim, num_heads)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Dropout(0.10),
            nn.Linear(embed_dim, 1)
        )
        if initial_bias is not None:
            with torch.no_grad():
                self.mlp[-1].bias.fill_(initial_bias)

    def forward(self, q_chunks, c_chunks):
        pooled_per_q = []
        for q in q_chunks:
            if q.ndim == 2:
                q = q.unsqueeze(0)
            ctx_logits = []
            for c in c_chunks:
                if c.ndim == 2:
                    c = c.unsqueeze(0)
                ctx_mask = (c.abs().sum(dim=-1) == 0)
                x = self.cross(q, c, context_mask=ctx_mask)
                logits = self.mlp(x).squeeze(0).squeeze(-1)
                ctx_logits.append(logits)
            pooled = torch.max(torch.stack(ctx_logits, dim=0), dim=0).values
            pooled_per_q.append(pooled)
        return pooled_per_q

def merge_chunk_logits_to_full(pooled_per_q, q_starts, full_len, device=device):
    out = torch.full((full_len,), -1e9, dtype=torch.float32, device=device)
    for vec, st in zip(pooled_per_q, q_starts):
        vec = vec.to(device)
        Lq = vec.shape[0]
        placed = torch.full((full_len,), -1e9, dtype=torch.float32, device=device)
        placed[st:st+Lq] = vec
        out = torch.maximum(out, placed)
    out[out <= -1e8] = -30.0
    return out

peptide_site_model = None
receptor_site_model = None

def _safe_torch_load(path, map_location=None):
    try:
        return torch.load(path, map_location=map_location)
    except TypeError:
        raise
    except Exception:
        return torch.load(path, map_location=map_location, weights_only=False)

def load_ppi_models():
    global peptide_site_model, receptor_site_model
    if peptide_site_model is None:
        m = ChunkwiseInteractionModel(embed_dim=EMBED_DIM, num_heads=NUM_HEADS).to(device)
        state = _safe_torch_load(PEPTIDE_MODEL_PATH, map_location=device)
        m.load_state_dict(state, strict=True)
        m.eval()
        peptide_site_model = m
    if receptor_site_model is None:
        m = ChunkwiseInteractionModel(embed_dim=EMBED_DIM, num_heads=NUM_HEADS).to(device)
        state = _safe_torch_load(RECEPTOR_MODEL_PATH, map_location=device)
        m.load_state_dict(state, strict=True)
        m.eval()
        receptor_site_model = m

def predict_query_given_context(query_seq, context_seq, model,
                                cache_query=True, cache_context=True):
    q_chunk_dicts, q_len = get_or_compute_embeddings(query_seq, allow_cache=cache_query)
    if cache_context:
        c_chunk_dicts, _ = get_or_compute_embeddings(context_seq, allow_cache=True)
    else:
        c_chunk_dicts, _ = embed_sequence_chunks(context_seq)
    q_chunks = [d["embedding"].to(device) for d in q_chunk_dicts]
    c_chunks = [d["embedding"].to(device) for d in c_chunk_dicts]
    q_starts = [int(d["start_idx"]) for d in q_chunk_dicts]
    if len(q_chunks) == 0 or len(c_chunks) == 0:
        return np.zeros(len(query_seq), dtype=float)
    with torch.no_grad():
        pooled_per_q = model(q_chunks, c_chunks)
        logits_full = merge_chunk_logits_to_full(pooled_per_q, q_starts, q_len)
        probs = torch.sigmoid(logits_full).cpu().numpy()
    if len(probs) > len(query_seq):
        probs = probs[:len(query_seq)]
    elif len(probs) < len(query_seq):
        probs = np.pad(probs, (0, len(query_seq) - len(probs)), "edge")
    return probs

def compute_scrambled_predictions_for_query(query_seq, partner_seq, model,
                                            num_scrambles=100, base_seed=0):
    all_scrambled = []
    for k in range(num_scrambles):
        seed = base_seed + k
        scrambled_partner = scramble_sequence(partner_seq, seed=seed)
        probs = predict_query_given_context(
            query_seq=query_seq,
            context_seq=scrambled_partner,
            model=model,
            cache_query=True,
            cache_context=False
        )
        all_scrambled.append(probs)
    return np.stack(all_scrambled, axis=0)

def compute_per_residue_z_and_p(real_pred, scrambled_pred_stack):
    mean_scr = np.mean(scrambled_pred_stack, axis=0)
    std_scr = np.std(scrambled_pred_stack, axis=0)
    std_scr[std_scr == 0] = 1e-6
    z_scores = (real_pred - mean_scr) / std_scr
    p_values = 1.0 - norm.cdf(z_scores)
    _, q_values = fdrcorrection(p_values, alpha=0.05)
    return z_scores, p_values, q_values

def save_predictions(filename, seq_id, partner_id, model_type, sequence, probabilities,
                     p_values=None, q_values=None, use_null_background=False):
    probs = np.asarray(probabilities, dtype=float)
    assert len(sequence) == len(probs), "sequence / probability length mismatch"
    with open(filename, "w") as f:
        f.write(f"# Query:{seq_id} Partner:{partner_id} Model:{model_type}\n")
        if use_null_background and p_values is not None and q_values is not None:
            f.write("Position\tAminoAcid\tProbability\tP-value\tFDR\n")
            for i, (aa, prob, p, q) in enumerate(zip(sequence, probs, p_values, q_values), 1):
                f.write(f"{i}\t{aa}\t{prob:.3f}\t{p:.4g}\t{q:.4g}\n")
        else:
            f.write("Position\tAminoAcid\tProbability\n")
            for i, (aa, prob) in enumerate(zip(sequence, probs), 1):
                f.write(f"{i}\t{aa}\t{prob:.3f}\n")

def predict_query_two_views(query_seq, partner_seq, cache_query=True, cache_partner=True):
    p_as_receptor = predict_query_given_context(
        query_seq=query_seq,
        context_seq=partner_seq,
        model=receptor_site_model,
        cache_query=cache_query,
        cache_context=cache_partner
    )
    p_as_peptide = predict_query_given_context(
        query_seq=query_seq,
        context_seq=partner_seq,
        model=peptide_site_model,
        cache_query=cache_query,
        cache_context=cache_partner
    )
    return p_as_receptor, p_as_peptide

def run_ppi_for_pair(query_id, query_seq, partner_id, partner_seq, output_dir, num_scrambles=5, use_null_background=False):
    print(f"  {query_id} \u2194 {partner_id}")
    t0 = time.perf_counter()
    p_rec, p_pep = predict_query_two_views(query_seq, partner_seq)
    rec_pvals = rec_qvals = None
    pep_pvals = pep_qvals = None
    if use_null_background:
        print("    Computing null background (query-as-receptor)...")
        scr_rec = compute_scrambled_predictions_for_query(
            query_seq=query_seq, partner_seq=partner_seq,
            model=receptor_site_model, num_scrambles=num_scrambles
        )
        _, rec_pvals, rec_qvals = compute_per_residue_z_and_p(p_rec, scr_rec)
        print("    Computing null background (query-as-peptide)...")
        scr_pep = compute_scrambled_predictions_for_query(
            query_seq=query_seq, partner_seq=partner_seq,
            model=peptide_site_model, num_scrambles=num_scrambles
        )
        _, pep_pvals, pep_qvals = compute_per_residue_z_and_p(p_pep, scr_pep)
    t1 = time.perf_counter()
    dt = t1 - t0
    safe_q = sanitize_filename(query_id)
    safe_p = sanitize_filename(partner_id)
    rec_file = os.path.join(output_dir, f"{safe_q}__{safe_p}__query_as_receptor.txt")
    pep_file = os.path.join(output_dir, f"{safe_q}__{safe_p}__query_as_peptide.txt")
    save_predictions(rec_file, query_id, partner_id, "query_as_receptor", query_seq, p_rec, rec_pvals, rec_qvals, use_null_background)
    save_predictions(pep_file, query_id, partner_id, "query_as_peptide", query_seq, p_pep, pep_pvals, pep_qvals, use_null_background)

def run_ppi_predictions(output_dir, query_text, partner_text, num_scrambles=5, use_null_background=False):
    seqs1 = parse_fasta(query_text)
    seqs2 = parse_fasta(partner_text)
    print(f"Parsed {len(seqs1)} query sequence(s) and {len(seqs2)} partner sequence(s).")
    if not seqs1 or not seqs2:
        print("No sequences found in one of the inputs.")
        return
    total_pairs = len(seqs1) * len(seqs2)
    pair_idx = 0
    for (i1, query_id, query_seq), (i2, partner_id, partner_seq) in product(seqs1, seqs2):
        pair_idx += 1
        print(f"[{pair_idx}/{total_pairs}] Query {query_id} vs Partner {partner_id}")
        run_ppi_for_pair(query_id, query_seq, partner_id, partner_seq,
                        output_dir=output_dir, num_scrambles=num_scrambles,
                        use_null_background=use_null_background)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SPPIDER-seq Protein-Protein Interaction Predictor")
    
    # File Inputs
    parser.add_argument("--query", type=str, required=True, help="Path to query FASTA file")
    parser.add_argument("--partner", type=str, required=True, help="Path to partner FASTA file")
    parser.add_argument("--outdir", type=str, default="predictions", help="Directory to save results")
    
    # Model Settings
    parser.add_argument("--device", type=str, default="cuda", choices=["cuda", "cpu"], help="Device to run on")
    parser.add_argument("--scrambles", type=int, default=5, help="Number of scrambles for null background")
    parser.add_argument("--null_bg", action="store_true", help="Enable null background statistical calculation (slow)")

    args = parser.parse_args()

    # Update global device based on user input
    if args.device == "cuda" and not torch.cuda.is_available():
        print("Warning: CUDA requested but not available. Falling back to CPU.")
        device = torch.device("cpu")
    else:
        device = torch.device(args.device)

    # 1. Create output directory
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    # 2. Read the FASTA files
    with open(args.query, "r") as f:
        query_fasta_text = f.read()
    with open(args.partner, "r") as f:
        partner_fasta_text = f.read()

    # 3. Load the heavy models
    print(f"--- Loading Models on {device} ---")
    ensure_esm_loaded()
    load_ppi_models()

    # 4. Run the prediction engine
    print(f"--- Starting Predictions (Null Background: {args.null_bg}) ---")
    run_ppi_predictions(
        output_dir=args.outdir,
        query_text=query_fasta_text,
        partner_text=partner_fasta_text,
        num_scrambles=args.scrambles,
        use_null_background=args.null_bg
    )
    print(f"--- Finished! Results saved to: {args.outdir} ---")