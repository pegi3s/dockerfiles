#!/bin/sh
# Entrypoint for the kcells Docker image.
#
# There are no defaults: every analysis parameter must be given, so the user
# always knows which settings were used. Images are read from /app/input and
# results written to /app/output (mount host folders there with -v).
#
# Two usage styles:
#   1. Environment variables (all required):
#        docker run --rm --user "$(id -u):$(id -g)" \
#            -v "$(pwd)/images:/app/input:ro" -v "$(pwd)/results:/app/output" \
#            -e K=4 -e FEATURES=texture,gradient,chromatin -e CLUSTER_METHOD=kmeans \
#            -e N_UNUSUAL=3 -e BORDER_CELLS=exclude -e CELLPOSE_DIAMETER=auto \
#            pegi3s/kcells:latest
#   2. Command-line arguments after the image name (passed to cell_pipeline.py
#      as they are; all of them required too):
#        docker run ... pegi3s/kcells:latest --input /app/input --output-dir /app/output \
#            --k 4 --features texture,gradient,chromatin --cluster-method kmeans \
#            --n-unusual 3 --border-cells exclude --cellpose-diameter auto
set -e

if [ "$#" -gt 0 ]; then
    exec python cell_pipeline.py "$@"
fi

missing=""
for var in K FEATURES CLUSTER_METHOD N_UNUSUAL BORDER_CELLS CELLPOSE_DIAMETER; do
    eval "value=\${$var:-}"
    [ -n "$value" ] || missing="$missing $var"
done
if [ -n "$missing" ]; then
    echo "error: missing required environment variable(s):$missing" >&2
    echo "  K                  number of cell clusters, e.g. 4" >&2
    echo "  FEATURES           comma-separated: shape,color,texture,gradient,density,chromatin, or all" >&2
    echo "  CLUSTER_METHOD     ward, kmeans or gmm" >&2
    echo "  N_UNUSUAL          number of most unusual cells to mark (0 = none)" >&2
    echo "  BORDER_CELLS       include or exclude (cells cut by the image edge)" >&2
    echo "  CELLPOSE_DIAMETER  typical cell diameter in pixels, or auto" >&2
    exit 2
fi

exec python cell_pipeline.py --input /app/input --output-dir /app/output \
    --k "$K" --features "$FEATURES" --cluster-method "$CLUSTER_METHOD" \
    --n-unusual "$N_UNUSUAL" --border-cells "$BORDER_CELLS" --cellpose-diameter "$CELLPOSE_DIAMETER"
