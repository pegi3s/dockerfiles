"""
ISPRED4 predictor — standalone script.

Based on the code from https://github.com/pegi3s/cport and
https://github.com/haddocking/cport (Apache 2.0 license).

Usage:
    python ispred4.py <pdb_file> --chain <chain_id> [--output <output_csv>]

Examples:
    python ispred4.py /data/input.pdb --chain A --output /data/output.ispred4.csv
    python ispred4.py --data-dir /data --chain A

If run without a PDB file argument, the script scans /data for *.pdb files
and processes every one of them using chain A by default, or another chain
specified with --chain. Results are written to /data/<stem>.ispred4.csv.

Environment variables:
    ISPRED4_WAIT_INTERVAL   seconds between polling attempts (default 60)
    ISPRED4_NUM_RETRIES     maximum number of polling attempts (default 36)
"""

import argparse
import logging
import os
import re
import sys
import tempfile
import time
from pathlib import Path
from urllib import request

import mechanicalsoup as ms
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ISPRED4_URL = "https://ispred4.biocomp.unibo.it/ispred/default/"

WAIT_INTERVAL = int(os.environ.get("ISPRED4_WAIT_INTERVAL", 60))
NUM_RETRIES = int(os.environ.get("ISPRED4_NUM_RETRIES", 36))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Core class (adapted from pegi3s/cport)
# ---------------------------------------------------------------------------

class Ispred4:
    """Submit a PDB chain to ISPRED4 and retrieve the interface-residue
    predictions as a pandas DataFrame."""

    def __init__(self, pdb_file: str, chain_id: str) -> None:
        self.pdb_file = pdb_file
        self.chain_id = chain_id
        self.wait = WAIT_INTERVAL
        self.tries = NUM_RETRIES

    # ------------------------------------------------------------------
    def submit(self) -> str:
        """Submit the job and return the summary-page URL."""
        log.info(f"Submitting {self.pdb_file} (chain {self.chain_id}) to ISPRED4 …")
        browser = ms.StatefulBrowser()
        browser.open(ISPRED4_URL)

        form = browser.select_form(nr=0)
        form.set(name="ispred_chain", value=self.chain_id)
        form.set(name="ispred_rsath", value="0.20")   # default RSA threshold

        with open(self.pdb_file, "rb") as fh:
            form.set(name="structure", value=fh)
            browser.submit_selected()

        # Extract job-id from the response page
        # https://regex101.com/r/KFLLil/1
        matches = re.findall(r"Jobid:.*?;\">(.*?)</div>", str(browser.page))
        if not matches:
            log.error("ISPRED4 submission failed — could not find job id in response.")
            sys.exit(1)

        job_id = matches[0]
        browser.close()

        summary_url = f"{ISPRED4_URL}job_summary?jobid={job_id}"
        log.info(f"Job submitted. Summary URL: {summary_url}")
        return summary_url

    # ------------------------------------------------------------------
    def retrieve_prediction_link(self, url: str) -> str:
        """Poll the summary page until the job completes and return the
        download URL."""
        # https://regex101.com/r/ulO1lf/1
        job_id = re.findall(r"id=(.*)", url)[0]

        log.info(
            f"Polling for results (max {self.tries} attempts, "
            f"{self.wait}s interval) …"
        )
        browser = ms.StatefulBrowser()
        browser.open(url)

        while self.tries > 0:
            # While the job is running the completion timestamp shows "--"
            # https://regex101.com/r/fK3U6b/1
            if not re.findall(r">--<", str(browser.page)):
                log.info("Job completed.")
                break

            log.debug(f"Still running — {self.tries} attempts left …")
            time.sleep(self.wait)
            browser.open(url)
            self.tries -= 1
        else:
            log.error(f"ISPRED4 server did not respond in time. URL: {url}")
            sys.exit(1)

        browser.close()
        return f"{ISPRED4_URL}downloadjob?jobid={job_id}"

    # ------------------------------------------------------------------
    @staticmethod
    def download_result(download_link: str) -> str:
        """Download the result file to a temporary location and return its
        path."""
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        log.info(f"Downloading result from {download_link} …")
        request.urlretrieve(download_link, tmp.name)
        return tmp.name

    # ------------------------------------------------------------------
    @staticmethod
    def parse_prediction(result_file: str) -> pd.DataFrame:
        """Parse the raw ISPRED4 output file and return a DataFrame.

        Expected columns include:
            ResNum, ResType, RSA, Score, Probability, Inter

        Rows are classified as:
            Inter == 'yes'  → active/interface residue
            Inter == 'no'   → passive/surface non-interface residue
            buried residues have no Inter value and may be omitted downstream
        """
        # The file has 15 header lines before the data table
        df = pd.read_csv(result_file, skiprows=15, sep=r"\s+", engine="python")
        return df

    # ------------------------------------------------------------------
    def run(self) -> pd.DataFrame:
        """End-to-end execution: submit → poll → download → parse."""
        log.info(
            f"Running ISPRED4 for {self.pdb_file}, chain {self.chain_id} "
            f"(up to {self.tries} retries, {self.wait}s interval)"
        )
        summary_url = self.submit()
        download_link = self.retrieve_prediction_link(url=summary_url)
        result_file = self.download_result(download_link)
        df = self.parse_prediction(result_file)

        try:
            os.unlink(result_file)
        except OSError:
            pass

        return df


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def save_results(df: pd.DataFrame, output_path: str) -> None:
    """Save the prediction DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    log.info(f"Results saved to {output_path}")

def save_interface_residues_csv(df: pd.DataFrame, output_path: str) -> None:
    """Save a simplified residue-level CSV compatible with previous outputs.

    Output columns:
        res_num; res_name; ispred4_probability; code

    Mapping:
        ispred4_probability = ISPRED4 Probability
        code:
            ispred4_probability >= 0.50       -> 1
            ispred4_probability <= 0.25       -> 2
            0.25 < ispred4_probability < 0.50 -> 0
    """
    required_cols = {"ResNum", "ResType", "Probability"}
    missing_cols = required_cols - set(df.columns)

    if missing_cols:
        log.warning(
            f"Cannot generate simplified CSV. Missing columns: {sorted(missing_cols)}"
        )
        return

    rows = []

    for _, row in df.iterrows():
        try:
            res_num = int(row["ResNum"])
            res_name = str(row["ResType"]).strip()
            ispred4_probability = float(row["Probability"])
        except (ValueError, TypeError):
            continue

        if ispred4_probability >= 0.5:
            code = 1
        elif ispred4_probability <= 0.25:
            code = 2
        else:
            code = 0

        rows.append((res_num, res_name, f"{ispred4_probability:.2f}", code))

    if not rows:
        log.warning("No valid residues found for simplified CSV.")
        return

    simplified_df = pd.DataFrame(
        rows,
        columns=["res_num", "res_name", "ispred4_probability", "code"]
    )

    simplified_df.to_csv(output_path, sep=";", index=False)
    log.info(f"Simplified interface CSV saved to {output_path}")


def process_pdb(pdb_file: str, chain_id: str, output_path: str) -> None:
    """Run ISPRED4 for a single PDB file and save the CSV."""
    predictor = Ispred4(pdb_file=pdb_file, chain_id=chain_id)
    df = predictor.run()

    if df.empty:
        log.warning(f"No predictions returned for {pdb_file}.")
        return

    save_results(df, output_path)
    
    simplified_output = str(Path(output_path).with_suffix("")) + ".interface_residues.csv"
    save_interface_residues_csv(df, simplified_output)

    # Print a brief summary
    if "Inter" in df.columns:
        active = (df["Inter"] == "yes").sum()
        passive = (df["Inter"] == "no").sum()
        log.info(f"  Active residues : {active}")
        log.info(f"  Passive residues: {passive}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run ISPRED4 predictions for one or more PDB files."
    )
    parser.add_argument(
        "pdb_file",
        nargs="?",
        help="Path to the PDB file. If omitted, all *.pdb files in /data are processed.",
    )
    parser.add_argument(
        "--chain",
        default="A",
        help="Chain identifier to analyse (default: A).",
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output CSV file path. Only used when a single PDB file is provided. "
            "Defaults to <pdb_stem>.ispred4.csv in the same directory."
        ),
    )
    parser.add_argument(
        "--data-dir",
        default="/data",
        help="Directory scanned for *.pdb files when no pdb_file argument is given (default: /data).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.pdb_file:
        # Single-file mode
        pdb_path = Path(args.pdb_file)
        if not pdb_path.is_file():
            log.error(f"PDB file not found: {pdb_path}")
            sys.exit(1)

        output = args.output or str(pdb_path.with_suffix("")) + ".ispred4.csv"
        process_pdb(str(pdb_path), args.chain, output)

    else:
        # Batch mode: scan data_dir for *.pdb files
        data_dir = Path(args.data_dir)
        pdb_files = sorted(data_dir.glob("*.pdb"))

        if not pdb_files:
            log.error(f"No *.pdb files found in {data_dir}.")
            sys.exit(1)

        log.info(f"Found {len(pdb_files)} PDB file(s) in {data_dir}.")
        for pdb_path in pdb_files:
            output = str(data_dir / (pdb_path.stem + ".ispred4.csv"))
            process_pdb(str(pdb_path), args.chain, output)


if __name__ == "__main__":
    main()
