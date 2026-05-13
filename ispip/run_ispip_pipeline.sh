#!/bin/bash
set -e

INPUT=""
OUTPUT_DIR=""

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -i|--input)
            INPUT="$2"
            shift 2
            ;;
        -of|--output-folder|--output_dir|--output-dir)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage:"
            echo "  docker run --rm -v /your/data/dir:/data pegi3s/ispip -i /data/input.csv -of /data/output"
            echo ""
            echo "Arguments:"
            echo "  -i, --input          Input CSV file"
            echo "  -of, --output-folder Output directory"
            echo ""
            echo "This wrapper runs ISPIP in two steps:"
            echo "  1. generate mode: creates .joblib model files"
            echo "  2. predict mode: uses those .joblib files to generate predictions"
            exit 0
            ;;
        *)
            echo "ERROR: Unknown argument: $1"
            echo "Run with --help for usage."
            exit 1
            ;;
    esac
done

if [ -z "$INPUT" ]; then
    echo "ERROR: input CSV is required."
    echo "Usage: docker run --rm -v /your/data/dir:/data pegi3s/ispip -i /data/input.csv -of /data/output"
    exit 1
fi

if [ -z "$OUTPUT_DIR" ]; then
    echo "ERROR: output folder is required."
    echo "Usage: docker run --rm -v /your/data/dir:/data pegi3s/ispip -i /data/input.csv -of /data/output"
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "ERROR: input CSV not found: $INPUT"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR/models"
mkdir -p "$OUTPUT_DIR/predictions"

echo "==> ISPIP pipeline started"
echo "Input CSV: $INPUT"
echo "Output directory: $OUTPUT_DIR"
echo ""

echo "==> Step 1/2: generating ISPIP model files..."
python3 /opt/ispip/main.py \
    -i "$INPUT" \
    -of "$OUTPUT_DIR/models" \
    --mode generate

echo ""
echo "==> Step 2/2: running ISPIP predictions..."
python3 /opt/ispip/main.py \
    -i "$INPUT" \
    -if "$OUTPUT_DIR/models" \
    -of "$OUTPUT_DIR/predictions" \
    --mode predict

echo ""
echo "==> ISPIP pipeline completed."
echo "Models saved to: $OUTPUT_DIR/models"
echo "Predictions saved to: $OUTPUT_DIR/predictions"

touch "$OUTPUT_DIR/ispip_pipeline_done.txt"
