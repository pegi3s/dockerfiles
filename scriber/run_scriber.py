#!/usr/bin/env python3
"""
Standalone script to submit a PDB chain to the SCRIBER server and retrieve results.

SCRIBER predicts protein-protein interaction sites from sequence.
Server: https://biomine2.cs.vcu.edu/servers/SCRIBER/

Usage:
    python run_scriber.py <pdb_file> <chain_id> [--output-dir <output_dir>]

Example:
    python run_scriber.py /data/atxn3wt_IT.pdb A --output-dir /output

This script creates:
    1. SCRIBER raw-style CSV:
        <protein_name>.scriber.csv

    2. Simplified residue-level CSV:
        <protein_name>.scriber.interface_residues.csv

Important:
    SCRIBER residue numbers are treated as sequence positions, not as original
    PDB residue numbers. The script maps each SCRIBER sequence position back
    to the corresponding residue number in the original PDB file.
"""

import argparse
import logging
import os
import re
import sys
import tempfile
import time
import warnings
from urllib import request

import mechanicalsoup as ms
import pandas as pd
from Bio import BiopythonWarning, SeqIO

warnings.simplefilter("ignore", BiopythonWarning)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIBER_URL = os.environ.get(
    "SCRIBER_URL",
    "https://biomine2.cs.vcu.edu/servers/SCRIBER/"
)

WAIT_INTERVAL = int(os.environ.get("SCRIBER_WAIT_INTERVAL", 30))
NUM_RETRIES = int(os.environ.get("SCRIBER_NUM_RETRIES", 36))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

log = logging.getLogger("scriber")


AA_3TO1 = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
    "SEC": "U", "PYL": "O", "ASX": "B", "GLX": "Z", "XLE": "J",
    "UNK": "X",
}


# ---------------------------------------------------------------------------
# PDB / sequence helpers
# ---------------------------------------------------------------------------

def get_fasta_from_pdbfile(pdb_file: str, chain_id: str) -> str:
    """
    Extract the amino-acid sequence for chain_id from a PDB file.
    """
    sequence = None

    with open(pdb_file) as handle:
        for record in SeqIO.PdbIO.PdbAtomIterator(handle):
            if record.id.endswith(chain_id) or record.id[-1] == chain_id:
                sequence = str(record.seq)

    if sequence is None:
        log.error("Chain '%s' not found in %s", chain_id, pdb_file)
        sys.exit(1)

    return sequence


def read_pdb_residue_sequence(pdb_file: str, chain_id: str) -> list:
    """
    Read residues from a PDB file and return an ordered list.

    Output format:
        [
            {
                "seq_pos": 1,
                "pdb_res_num": "214",
                "res_name": "M"
            },
            ...
        ]
    """
    residues = []
    seen = set()

    with open(pdb_file, "r") as f:
        for line in f:
            if not line.startswith("ATOM"):
                continue

            chain = line[21].strip()
            if chain != chain_id:
                continue

            res_num = line[22:26].strip()
            insertion_code = line[26].strip()
            res_name_3 = line[17:20].strip().upper()

            if not res_num:
                continue

            residue_id = (chain, res_num, insertion_code)

            if residue_id in seen:
                continue

            seen.add(residue_id)

            pdb_res_num = f"{res_num}{insertion_code}" if insertion_code else res_num
            res_name = AA_3TO1.get(res_name_3, "X")

            residues.append(
                {
                    "seq_pos": len(residues) + 1,
                    "pdb_res_num": pdb_res_num,
                    "res_name": res_name,
                }
            )

    if not residues:
        log.error("No ATOM residues found for chain '%s' in %s", chain_id, pdb_file)
        sys.exit(1)

    return residues


def validate_sequence_mapping(pdb_file: str, chain_id: str) -> None:
    """
    Compare the sequence length extracted by Biopython with the number of
    unique ATOM residues read manually from the PDB.
    """
    fasta_seq = get_fasta_from_pdbfile(pdb_file, chain_id)
    pdb_residues = read_pdb_residue_sequence(pdb_file, chain_id)

    fasta_len = len(fasta_seq)
    residue_count = len(pdb_residues)

    log.info("Extracted FASTA sequence length: %d", fasta_len)
    log.info("Mapped PDB residue count: %d", residue_count)

    if fasta_len != residue_count:
        log.warning(
            "Sequence length and mapped PDB residue count differ. "
            "FASTA length = %d, PDB residue count = %d. "
            "The output may require manual inspection.",
            fasta_len,
            residue_count,
        )


# ---------------------------------------------------------------------------
# SCRIBER interaction
# ---------------------------------------------------------------------------

def submit(pdb_file: str, chain_id: str) -> str:
    """
    Submit a FASTA sequence to SCRIBER and return the result-status URL.
    """
    fasta_seq = get_fasta_from_pdbfile(pdb_file, chain_id)

    if "X" in fasta_seq:
        log.warning(
            "The extracted sequence contains X residues. "
            "They will be kept to preserve sequence-to-PDB mapping. "
            "If SCRIBER rejects the submission, inspect the PDB sequence manually."
        )

    submission_string = f">Chain {chain_id}\n{fasta_seq}"

    log.info("Submitting chain '%s' to SCRIBER: %s", chain_id, SCRIBER_URL)
    log.info("Submitted sequence length: %d residues", len(fasta_seq))

    browser = ms.StatefulBrowser()
    browser.open(SCRIBER_URL)

    form = browser.select_form(nr=0)
    form.set(name="seq", value=submission_string)
    form.set(name="email1", value="")
    browser.submit_selected(btnName="Button1")

    links = browser.links()
    browser.close()

    matches = re.findall(r'(https?://[^\s"\'<>]+)', str(links))

    if not matches:
        log.error("SCRIBER submission failed — could not find result URL in response.")
        sys.exit(1)

    submitted_url = matches[0]
    log.info("Job submitted. Polling URL: %s", submitted_url)

    return submitted_url


def retrieve_result_csv_link(submitted_url: str) -> str:
    """
    Poll submitted_url until a .csv result link appears, then return it.
    """
    browser = ms.StatefulBrowser()
    browser.open(submitted_url)

    tries = NUM_RETRIES

    while True:
        match = re.search(r"(https?://[^\s\"'<>]*\.csv)", str(browser.page))

        if match:
            result_csv_link = match.group(1)
            browser.close()
            log.info("Results ready: %s", result_csv_link)
            return result_csv_link

        tries -= 1

        if tries <= 0:
            browser.close()
            log.error(
                "SCRIBER did not return results after %d retries (%ds each). URL: %s",
                NUM_RETRIES,
                WAIT_INTERVAL,
                submitted_url,
            )
            sys.exit(1)

        log.info("Waiting for SCRIBER results... (%d retries left)", tries)
        time.sleep(WAIT_INTERVAL)
        browser.refresh()


def download_result(download_link: str) -> str:
    """
    Download the SCRIBER CSV result file to a temporary path.
    """
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    tmp.close()

    request.urlretrieve(download_link, tmp.name)

    log.info("Result file downloaded to: %s", tmp.name)
    return tmp.name


def parse_prediction(result_file: str) -> dict:
    """
    Parse the SCRIBER CSV output.

    SCRIBER uses uppercase/lowercase residue letters in its output:
        uppercase -> active/interface
        lowercase -> passive/non-interface
    """
    df = pd.read_csv(
        result_file,
        skiprows=2,
        usecols=[0, 1, 4],
        header=None,
    )

    df.columns = ["ResidueNumber", "ResidueType", "ResidueScore"]

    prediction = {"active": [], "passive": []}

    for row in df.itertuples():
        residue_type = str(row.ResidueType)

        if residue_type.isupper():
            prediction["active"].append([row.ResidueNumber, row.ResidueScore])
        elif residue_type.islower():
            prediction["passive"].append([row.ResidueNumber, row.ResidueScore])
        else:
            log.warning("Skipping unprocessable residue row: %s", row)

    return prediction


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def save_results(prediction: dict, output_path: str) -> None:
    """
    Write SCRIBER prediction as a raw-style CSV file.

    Output columns:
        residue,score,classification

    Here, 'residue' is the SCRIBER sequence position.
    """
    rows = []

    for residue_num, score in prediction["active"]:
        rows.append(
            {
                "residue": residue_num,
                "score": score,
                "classification": "active",
            }
        )

    for residue_num, score in prediction["passive"]:
        rows.append(
            {
                "residue": residue_num,
                "score": score,
                "classification": "passive",
            }
        )

    if not rows:
        log.warning("Prediction dictionary is empty — no rows to save.")
        return

    result_df = pd.DataFrame(rows)

    result_df["residue_numeric"] = pd.to_numeric(
        result_df["residue"],
        errors="coerce",
    )

    result_df = (
        result_df
        .sort_values("residue_numeric")
        .drop(columns=["residue_numeric"])
        .reset_index(drop=True)
    )

    result_df.to_csv(output_path, index=False)

    log.info("Raw SCRIBER-style results saved to: %s", output_path)


def save_interface_residues_csv(
    prediction: dict,
    pdb_file: str,
    chain_id: str,
    output_csv: str,
) -> None:
    """
    Save simplified residue-level CSV.

    Output columns:
        seq_pos;res_num;res_name;scriber_score;code

    Mapping:
        active  -> code 1
        passive -> code 2
    """
    pdb_residues = read_pdb_residue_sequence(pdb_file, chain_id)

    rows = []

    for residue_num, score in prediction["active"]:
        try:
            seq_pos = int(float(residue_num))
            score_float = float(score)

            if pd.isna(seq_pos) or pd.isna(score_float):
                continue

        except (ValueError, TypeError):
            continue

        index = seq_pos - 1

        if index < 0 or index >= len(pdb_residues):
            log.warning(
                "SCRIBER residue position %s is outside mapped PDB residue list length %d",
                seq_pos,
                len(pdb_residues),
            )
            continue

        pdb_residue = pdb_residues[index]

        rows.append(
            (
                seq_pos,
                pdb_residue["pdb_res_num"],
                pdb_residue["res_name"],
                f"{score_float:.2f}",
                1,
            )
        )

    for residue_num, score in prediction["passive"]:
        try:
            seq_pos = int(float(residue_num))
            score_float = float(score)

            if pd.isna(seq_pos) or pd.isna(score_float):
                continue

        except (ValueError, TypeError):
            continue

        index = seq_pos - 1

        if index < 0 or index >= len(pdb_residues):
            log.warning(
                "SCRIBER residue position %s is outside mapped PDB residue list length %d",
                seq_pos,
                len(pdb_residues),
            )
            continue

        pdb_residue = pdb_residues[index]

        rows.append(
            (
                seq_pos,
                pdb_residue["pdb_res_num"],
                pdb_residue["res_name"],
                f"{score_float:.2f}",
                2,
            )
        )

    if not rows:
        log.warning("No rows available for simplified interface CSV.")
        return

    out_df = pd.DataFrame(
        rows,
        columns=[
            "seq_pos",
            "res_num",
            "res_name",
            "scriber_score",
            "code",
        ],
    )

    out_df = out_df.sort_values("seq_pos").reset_index(drop=True)

    out_df.to_csv(output_csv, sep=";", index=False)

    log.info("Simplified interface CSV saved to: %s", output_csv)


def get_default_raw_output_path(pdb_file: str, output_dir: str = ".") -> str:
    """
    Create the default raw SCRIBER output path.

    Example:
        pdb_file = /data/atxn3wt_IT.pdb
        output_dir = /output

    returns:
        /output/atxn3wt_IT.scriber.csv
    """
    protein_name = os.path.splitext(os.path.basename(pdb_file))[0]

    return os.path.join(
        output_dir,
        f"{protein_name}.scriber.csv"
    )


def get_default_interface_output_path(pdb_file: str, output_dir: str = ".") -> str:
    """
    Create the default simplified SCRIBER interface-residues output path.

    Example:
        pdb_file = /data/atxn3wt_IT.pdb
        output_dir = /output

    returns:
        /output/atxn3wt_IT.scriber.interface_residues.csv
    """
    protein_name = os.path.splitext(os.path.basename(pdb_file))[0]

    return os.path.join(
        output_dir,
        f"{protein_name}.scriber.interface_residues.csv"
    )


def print_acknowledgement() -> None:
    """
    Print SCRIBER acknowledgement and license reminder.
    """
    print("\n--- Acknowledgement and License Reminder ---")
    print("Results were generated using the SCRIBER server from the Biomine Lab.")
    print("Please cite SCRIBER and the underlying method(s) in any publication.")
    print("Use is subject to the Biomine Lab disclaimer and license agreement.")
    print("This script does not include or redistribute the SCRIBER software.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Submit a PDB chain to the SCRIBER server and retrieve predictions."
    )

    parser.add_argument("pdb_file", help="Path to the input PDB file")
    parser.add_argument("chain_id", help="Chain identifier, e.g. A")

    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Optional path for the SCRIBER raw-style output CSV",
    )

    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for SCRIBER result files",
    )

    parser.add_argument(
        "--interface-output",
        default=None,
        help="Optional path for the simplified interface-residues CSV",
    )

    args = parser.parse_args()

    if not os.path.isfile(args.pdb_file):
        log.error("PDB file not found: %s", args.pdb_file)
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)

    validate_sequence_mapping(args.pdb_file, args.chain_id)

    submitted_url = submit(args.pdb_file, args.chain_id)
    result_csv_url = retrieve_result_csv_link(submitted_url)
    result_file = download_result(result_csv_url)

    prediction = parse_prediction(result_file)

    try:
        os.unlink(result_file)
    except OSError:
        pass

    active_count = len(prediction["active"])
    passive_count = len(prediction["passive"])

    log.info(
        "Prediction complete — active: %d residues, passive: %d residues",
        active_count,
        passive_count,
    )

    # ----- Output handling -----
    # args.output can be either:
    # 1) a CSV file path, e.g. /data/results/scriber_results.csv
    # 2) an output directory, e.g. /data/results
    # If --output is not provided, --output-dir is used.

    protein_name = os.path.splitext(os.path.basename(args.pdb_file))[0]

    if args.output is None:
        output_dir = args.output_dir
        results_output = os.path.join(
            output_dir,
            f"{protein_name}.scriber_results.csv"
        )
    elif args.output.lower().endswith(".csv"):
        results_output = args.output
        output_dir = os.path.dirname(results_output) or "."
    else:
        output_dir = args.output
        results_output = os.path.join(
            output_dir,
            f"{protein_name}.scriber_results.csv"
        )

    os.makedirs(output_dir, exist_ok=True)

    interface_output = args.interface_output or os.path.join(
        output_dir,
        f"{protein_name}.scriber.interface_residues.csv"
    )

    save_results(prediction, results_output)

    save_interface_residues_csv(
        prediction=prediction,
        pdb_file=args.pdb_file,
        chain_id=args.chain_id,
        output_csv=interface_output,
    )

    print("\n--- SCRIBER Prediction Summary ---")
    print(f"Active residues : {active_count}")
    print(f"Passive residues: {passive_count}")
    print(f"Raw results saved to: {results_output}")
    print(f"Simplified CSV saved to: {interface_output}")
    print("Simplified CSV columns:")
    print("  seq_pos       = position in the sequence submitted to SCRIBER")
    print("  res_num       = original residue number in the PDB file")
    print("  res_name      = one-letter amino-acid code from the PDB file")
    print("  scriber_score = SCRIBER prediction score")
    print("  code          = 1 for active/interface, 2 for passive/non-interface")
    print_acknowledgement()


if __name__ == "__main__":
    main()