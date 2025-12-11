# Building instructions

Run:

```bash
CURRENT_VERSION=2.17.0 && docker build ./ -t pegi3s/blast:${CURRENT_VERSION} --build-arg VERSION=${CURRENT_VERSION} && docker tag pegi3s/blast:${CURRENT_VERSION} pegi3s/blast:latest
```

# Build log

- 2.14.0 - 08/05/2023 - Hugo López Fernández
- 2.15.0_v1 - 20/11/2023 - Docker Hub automated build (Re-tagged manually from 2.15.0 to install new libraries in the current 2.15.0)
- 2.17.0 - 11/12/2024 - Hugo López Fernández
