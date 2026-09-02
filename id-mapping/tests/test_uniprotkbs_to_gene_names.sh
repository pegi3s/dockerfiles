#!/bin/bash

# End-to-end test for pegi3s/id-mapping map-ids.
# Maps the UniProtKB AC/ID in test_data/ids.txt to gene names and checks that
# the output equals test_data/uniprotkbs_to_gene_names_mapping.tsv.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

IMAGE="${IMAGE:-pegi3s/id-mapping}"

OUTPUT_DIR="$(mktemp -d /tmp/id-mapping-test.XXXXXX)"
trap 'rm -rf "$OUTPUT_DIR"' EXIT

docker run --rm \
    -v "$ROOT_DIR":/data \
    -v "$OUTPUT_DIR":/output \
    -w /data \
    "$IMAGE" \
    map-ids --from-db UniProtKB_AC-ID --to-db Gene_Name --input test_data/ids.txt \
        --batch-size 2 --output /output/uniprotkbs_to_gene_names_mapping.tsv

if cmp --silent "$ROOT_DIR/test_data/uniprotkbs_to_gene_names_mapping.tsv" "$OUTPUT_DIR/uniprotkbs_to_gene_names_mapping.tsv"; then
    echo "[test] uniprotkbs-to-gene-names SUCCESS"
else
    echo "[test] uniprotkbs-to-gene-names FAILED"
    diff "$ROOT_DIR/test_data/uniprotkbs_to_gene_names_mapping.tsv" "$OUTPUT_DIR/uniprotkbs_to_gene_names_mapping.tsv" || true
    exit 1
fi