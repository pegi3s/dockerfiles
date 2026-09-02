#!/bin/bash

# End-to-end test for pegi3s/id-mapping gene-id-to-uniprotkb.
# Maps the gene IDs in test_data/gene_ids.txt to UniProtKB and checks that the
# output equals test_data/gene_ids_to_uniprotkbs_mapping.tsv.

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
    gene-id-to-uniprotkb test_data/gene_ids.txt /output/gene_ids_to_uniprotkbs_mapping.tsv \
    --output-format tsv --quiet

if cmp --silent "$ROOT_DIR/test_data/gene_ids_to_uniprotkbs_mapping.tsv" "$OUTPUT_DIR/gene_ids_to_uniprotkbs_mapping.tsv"; then
    echo "[test] gene-id-to-uniprotkb SUCCESS"
else
    echo "[test] gene-id-to-uniprotkb FAILED"
    diff "$ROOT_DIR/test_data/gene_ids_to_uniprotkbs_mapping.tsv" "$OUTPUT_DIR/gene_ids_to_uniprotkbs_mapping.tsv" || true
    exit 1
fi