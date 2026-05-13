#!/usr/bin/env python3
import os
import sys

import warnings
from Bio import BiopythonWarning
from Bio.PDB.PDBExceptions import PDBConstructionWarning

warnings.simplefilter("ignore", PDBConstructionWarning)
warnings.simplefilter("ignore", BiopythonWarning)

PIPENN_HOME = "/opt/pipenn/"
UTILS_PATH = os.path.join(PIPENN_HOME, "utils")

# Ensure PIPENN modules are importable before any local imports
for _p in [PIPENN_HOME, UTILS_PATH]:
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _generate_features_csv(fasta_file, features_csv, results_dir):
    """
    Calls GenerateMinFeatures logic directly (importing the module), but
    stops BEFORE the broken TFT5EncoderModel embedding step.
    """
    import GenerateMinFeatures as gmf
    from PPIDataset import DatasetParams

    DatasetParams.PIPENN_HOME = PIPENN_HOME
    DatasetParams.USER_INPUT_FASTA_FILE = fasta_file
    DatasetParams.USERDS_INPUT_DIR = results_dir + "/"
    DatasetParams.PREPARED_USERDS_FILE = features_csv

    prot_seqs, prot_lens, prot_ids = gmf.parseUseInput()
    df_inp = gmf.generateDFInput(prot_seqs, prot_lens, prot_ids)
    gmf.genPreparedPipennProtFiles(df_inp)


def _generate_embeddings(features_csv, results_dir):
    """
    Generates per-residue ProtT5 embeddings using the PyTorch T5EncoderModel
    (replaces the removed TFT5EncoderModel used by PPIDataset.createProtbertFile).
    Saves a .npz file that the prediction script loads via PROT_BERT_EMBEDDING_DIR.
    """
    import numpy as np
    import pandas as pd
    import torch
    from transformers import T5EncoderModel, T5Tokenizer
    from PPIDataset import DatasetParams

    # Must match what GenerateMinFeatures sets before calling createProtbertFile
    DatasetParams.SEQ_COLUMN_NAME = "sequence"

    model_name = "Rostlab/prot_t5_xl_uniref50"
    print(f"  Loading ProtT5 tokenizer and model...")
    tokenizer = T5Tokenizer.from_pretrained(model_name, do_lower_case=False)
    model = T5EncoderModel.from_pretrained(model_name)
    model.eval()

    dataset = pd.read_csv(features_csv)
    prot_ids = dataset[DatasetParams.PROT_ID_NAME].values   # 'uniprot_id'
    aavec = dataset[DatasetParams.SEQ_COLUMN_NAME].values.astype(str)  # 'sequence'

    emb_dict = {}
    with torch.no_grad():
        for prot_id, aa_str in zip(prot_ids, aavec):
            # CSV stores comma-separated AAs; ProtT5 expects space-separated
            prot_seq = aa_str.replace(",", " ")
            ids = tokenizer(
                prot_seq, add_special_tokens=True, return_tensors="pt"
            )
            input_ids = ids["input_ids"]
            attention_mask = ids["attention_mask"]
            out = model(input_ids=input_ids, attention_mask=attention_mask)
            emb = out.last_hidden_state.squeeze(0).numpy()  # (seq+1, 1024)
            prot_len = int(attention_mask.sum()) - 1        # drop EOS token
            emb_dict[prot_id] = emb[:prot_len]             # (protLen, 1024)
            print(f"  prot-id: {prot_id} | emb-shape: {emb_dict[prot_id].shape}")

    # PROT_BERT_EMBEDDING_DIR defaults to './' → prediction reads ./prepared_userds.npz
    npz_path = os.path.join(results_dir, "prepared_userds.npz")
    np.savez(npz_path, **emb_dict)
    print(f"  Embeddings saved: {npz_path}")


def generate_interface_residues_csv(results_dir):
    import glob
    import pandas as pd

    dnet_dir = os.path.join(results_dir, "dnet-ppi")
    csv_path = os.path.join(results_dir, "interface_residues.csv")

    pred_files = sorted(glob.glob(os.path.join(dnet_dir, "preds-*.csv")))

    if not pred_files:
        print("  No PIPENN prediction CSV files found in dnet-ppi.")
        return

    rows = []

    for pred_file in pred_files:
        df = pd.read_csv(pred_file)

        for _, row in df.iterrows():
            prot_id = row["prot_id"]
            seq = str(row["prot_seq"]).split(",")
            preds = [float(x) for x in str(row["y_preds"]).split(",")]

            if len(seq) != len(preds):
                print(f"  Warning: sequence length and prediction length differ for {prot_id}.")
                print(f"  Sequence length: {len(seq)} | Prediction length: {len(preds)}")
                continue

            for i, (aa, score) in enumerate(zip(seq, preds), start=1):
                if score >= 0.5:
                    code = 1
                elif score <= 0.25:
                    code = 2
                else:
                    code = 0

                rows.append((i, aa, f"{score:.2f}", code))

    if not rows:
        print("  No residues found for extra CSV.")
        return

    with open(csv_path, "w") as f:
        f.write("res_num; res_name; y_preds; code\n")
        for row in rows:
            f.write(";".join(str(x) for x in row) + "\n")

    print(f"  Extra CSV generated: {csv_path}")


def run_pipeline(input_pdb, output_dir=None):
    import subprocess
    from Bio import SeqIO

    pdb_path = os.path.abspath(input_pdb)
    pdb_name = os.path.splitext(os.path.basename(input_pdb))[0]
    results_dir = output_dir or "/data/pipenn-results"
    results_dir = os.path.abspath(results_dir)
    os.makedirs(results_dir, exist_ok=True)

    fasta_file = os.path.join(results_dir, f"{pdb_name}.fasta")
    features_csv = os.path.join(results_dir, "prepared_userds.csv")

    # --- Step 1: Extract sequence from PDB → FASTA ---
    print(f"\n[1/4] Extracting sequence from {pdb_name}...")
    seqs = []
    for record in SeqIO.parse(pdb_path, "pdb-atom"):
        seq_str = str(record.seq)
        if seq_str not in [s[1] for s in seqs]:
            seqs.append([record.id, seq_str])
    if not seqs:
        print("No sequences found in PDB file.")
        sys.exit(1)
    with open(fasta_file, "w") as f:
        for seq_id, seq in seqs:
            f.write(f">{seq_id}\n{seq}\n")
    print(f"  Found {len(seqs)} unique chain(s).")

    # --- Step 2: Generate feature CSV (skipping TF embedding step) ---
    print(f"\n[2/4] Generating feature CSV...")
    # CWD must be results_dir so that PROT_BERT_EMBEDDING_DIR='./' resolves correctly
    os.chdir(results_dir)
    _generate_features_csv(fasta_file, features_csv, results_dir)

    # --- Step 3: Generate ProtT5 embeddings via PyTorch ---
    print(f"\n[3/4] Generating ProtT5 embeddings (this may take a while)...")
    _generate_embeddings(features_csv, results_dir)

    # --- Step 4: Run PIPENN prediction ---
    # Script is called as: dnet-XD-ppi-keras.py <pipennHome> p
    # It reads ./prepared_userds.csv and ./prepared_userds.npz from CWD
    # PIPENN saves its output CSV to ./dnet-ppi/ relative to CWD
    os.makedirs(os.path.join(results_dir, "dnet-ppi"), exist_ok=True)
    print(f"\n[4/4] Running PIPENN-EMB Interface Prediction...")
    predict_cmd = [
        "python3",
        os.path.join(PIPENN_HOME, "dnet-ppi", "dnet-XD-ppi-keras.py"),
        PIPENN_HOME,
        "p",
    ]
    try:
        subprocess.run(predict_cmd, check=True, cwd=results_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error during prediction: {e}")
        sys.exit(1)

    print(f"\nGenerating extra interface residues CSV...")
    generate_interface_residues_csv(results_dir)

    print(f"\nSuccess! Results for {pdb_name} are in: {results_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: docker run ... pegi3s/pipenn /data/protein.pdb [output_dir]")
        print("Example: docker run --rm -v /your/data/dir:/data pegi3s/pipenn /data/input.pdb /data/results")
        sys.exit(1)

    input_pdb = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) >= 3 else None

    run_pipeline(input_pdb, output_dir)
