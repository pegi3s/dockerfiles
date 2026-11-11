# syntax=docker/dockerfile:1
FROM python:3.11-slim

LABEL org.opencontainers.image.title="kcells" \
      org.opencontainers.image.description="Cell-border segmentation, clustering and unusual-cell detection in microscopy images"

# System libraries needed by opencv-python-headless at runtime.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first so this layer is cached independently of
# source code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# numba (used by cellpose) caches compiled code next to its source by
# default, which fails for a non-root runtime user: use a writable dir.
ENV NUMBA_CACHE_DIR=/tmp/numba_cache
RUN mkdir -p /tmp/numba_cache && chmod 1777 /tmp/numba_cache

# Download the Cellpose cyto3 model at build time, to a fixed location, so
# the container runs offline and for any runtime user id.
ENV CELLPOSE_LOCAL_MODELS_PATH=/opt/cellpose
RUN mkdir -p /opt/cellpose \
    && python -c "from cellpose import models; models.Cellpose(gpu=False, model_type='cyto3')" \
    && chmod -R a+rX /opt/cellpose

COPY cell_pipeline.py ./
COPY object_pipeline/ object_pipeline/
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Default mount points for input images and results, writable by any uid so
# the container also works with `docker run --user <uid>:<gid>`.
RUN mkdir -p /app/input /app/output && chmod 1777 /app/input /app/output
VOLUME ["/app/input", "/app/output"]

# No analysis defaults: K, FEATURES, CLUSTER_METHOD, N_UNUSUAL, BORDER_CELLS and
# CELLPOSE_DIAMETER must be given at run time (see docker-entrypoint.sh).
ENV HOME=/tmp

ENTRYPOINT ["./docker-entrypoint.sh"]
