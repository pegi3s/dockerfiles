#!/usr/bin/env python3
"""CLI wrapper for SPPIDER-seq prediction.

This wrapper keeps the original SPPIDER-seq text outputs and also generates
a simplified residue-level CSV named interface_residues.csv.

The simplified CSV describes residues from the query sequence, evaluated
against the provided partner sequence(s). When SPPIDER-seq produces both
query_as_receptor and query_as_peptide views, both are preserved in the CSV
through the "model" column.
"""

import argparse
import glob
import os
import re
import sys

sys.path.insert(0, "/opt/SPPIDER-seq/notebooks")

from sppider_seq import (
    ensure_esm_loaded,
    load_ppi_models,
    run_ppi_predictions,
)


def _parse_prediction_header(header_line: str):
    """Parse SPPIDER-seq header lines.

    Expected format:
        # Query:<query_id> Partner:<partner_id> Model:<model_type>
    """
    pattern = r"#\s*Query:(.*?)\s+Partner:(.*?)\s+Model:(.*)"
    match = re.match(pattern, header_line.strip())
    if not match:
        return "", "", ""

    query_id = match.group(1).strip()
    partner_id = match.group(2).strip()
    model_type = match.group(3).strip()
    return query_id, partner_id, model_type


def generate_interface_residues_csv(output_dir: str) -> str:
    """Generate a simplified interface_residues.csv from SPPIDER-seq .txt outputs.

    Output columns:
        query_id;partner_id;model;res_num;res_name;sppiderseq_probability

    Notes:
        - res_num is the 1-based residue position in the query sequence.
        - res_name is the query residue one-letter amino-acid code.
        - model preserves the SPPIDER-seq view, usually query_as_receptor or
          query_as_peptide.
    """
    prediction_files = sorted(glob.glob(os.path.join(output_dir, "*.txt")))
    csv_path = os.path.join(output_dir, "interface_residues.csv")

    rows = []

    for prediction_file in prediction_files:
        with open(prediction_file, "r", encoding="utf-8") as handle:
            lines = [line.rstrip("\n") for line in handle]

        if not lines:
            continue

        query_id, partner_id, model_type = _parse_prediction_header(lines[0])

        for line in lines[1:]:
            line = line.strip()
            if not line or line.startswith("Position"):
                continue

            parts = line.split()
            if len(parts) < 3:
                continue

            try:
                res_num = int(parts[0])
                res_name = parts[1]
                probability = float(parts[2])
            except ValueError:
                continue

            rows.append(
                (
                    query_id,
                    partner_id,
                    model_type,
                    res_num,
                    res_name,
                    f"{probability:.3f}",
                )
            )

    if not rows:
        print("No SPPIDER-seq prediction rows found. interface_residues.csv was not generated.")
        return csv_path

    with open(csv_path, "w", encoding="utf-8") as handle:
        handle.write("query_id;partner_id;model;res_num;res_name;sppiderseq_probability\n")
        for row in rows:
            handle.write(";".join(str(value) for value in row) + "\n")

    print(f"Extra CSV generated: {csv_path}")
    return csv_path


def main():
    parser = argparse.ArgumentParser(description="SPPIDER-seq PPI site prediction")
    parser.add_argument("--query", required=True, help="Query FASTA file")
    parser.add_argument("--partner", required=True, help="Partner FASTA file(s)")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument(
        "--scrambles",
        type=int,
        default=0,
        help="Number of scrambles for null-background significance (default: 0 = off)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.query):
        print(f"Error: query file not found: {args.query}")
        sys.exit(1)
    if not os.path.exists(args.partner):
        print(f"Error: partner file not found: {args.partner}")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)

    print("Loading ESM-2 model...")
    ensure_esm_loaded()
    print("Loading PPI prediction models...")
    load_ppi_models()

    with open(args.query, "r", encoding="utf-8") as handle:
        query_text = handle.read()
    with open(args.partner, "r", encoding="utf-8") as handle:
        partner_text = handle.read()

    run_ppi_predictions(
        output_dir=args.output,
        query_text=query_text,
        partner_text=partner_text,
        num_scrambles=args.scrambles,
        use_null_background=args.scrambles > 0,
    )

    generate_interface_residues_csv(args.output)

    print(f"Done. Results saved to {args.output}")


if __name__ == "__main__":
    main()
