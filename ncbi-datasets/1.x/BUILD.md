# Building instructions

Specify the release version in `datasets_version` and run:

```bash
datasets_version=18.36.0 && docker build ./ -t pegi3s/ncbi-datasets:${datasets_version} --build-arg VERSION=${datasets_version}  && docker tag pegi3s/ncbi-datasets:${datasets_version} pegi3s/ncbi-datasets:latest

# Build log

- 18.36.0 - 24/08/2026 - Hugo López Fernandez
- 18.33.1 - 16/07/2026 - Hugo López Fernandez
- 18.32.0 - 10/07/2026 - Hugo López Fernández
- 18.7.0 - 15/09/2025 - Hugo López Fernández
- 16.12.1 - 30/04/2024 - Hugo López Fernández
