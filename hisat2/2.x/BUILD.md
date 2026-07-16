# Building instructions

Run:

```bash
HISAT2_VERSION=2.2.2 && \
    docker build ./ -t pegi3s/hisat2:${HISAT2_VERSION} --build-arg VERSION=${HISAT2_VERSION} && \
    docker tag pegi3s/hisat2:${HISAT2_VERSION} pegi3s/hisat2

# Build log

- 2.2.2 - 16/07/2026 - Hugo López Fernandez
- 2.2.0 - 13/06/2025 - Hugo López Fernández
- 2.1.0 - 13/06/2025 - Hugo López Fernández
