#!/bin/bash
set -e

# --- Directories ---
INPUT_DIR="/app/input"
OUTPUT_DIR="/app/output"
PESTO_DIR="/app/pesto"
TMPDIR=$(mktemp -d /tmp/pesto_work_XXXXXX)

echo "==> Temporary folder created: ${TMPDIR}"

# --- Delete temporary folder on exit ---
trap "rm -rf ${TMPDIR}" EXIT

# --- Check if there are input files ---
if [ -z "$(ls ${INPUT_DIR}/*.pdb 2>/dev/null)" ]; then
    echo "ERROR: No .pdb files found in ${INPUT_DIR}/"
    exit 1
fi

# --- Copy PDBs to the temporary folder ---
echo "==> Copying input files..."
cp ${INPUT_DIR}/*.pdb ${TMPDIR}/

# --- Create output folder ---
mkdir -p ${OUTPUT_DIR}

# --- Run PeSTo ---
echo "==> Running PeSTo model..."
cd ${PESTO_DIR}
python run_pesto.py ${TMPDIR}

# --- Copy only the _i0.pdb files to the output ---
echo "==> Copying results           ..."
cp ${TMPDIR}/*_i0.pdb ${OUTPUT_DIR}/

# --- Generate the interface residue CSV ---
echo "==> Generating CSV..."
python make_csv.py ${OUTPUT_DIR}

echo ""
echo "==> Completed! Files in ${OUTPUT_DIR}:"
ls -lh ${OUTPUT_DIR}/
