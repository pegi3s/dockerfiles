# Building instructions

Run:

```bash
CURRENT_VERSION=$(cat current.version) && docker build ./ -t pegi3s/id-mapping:${CURRENT_VERSION} --build-arg version=${CURRENT_VERSION} && docker tag pegi3s/id-mapping:${CURRENT_VERSION} pegi3s/id-mapping:latest
```

# Build log

- 1.1.1 - 02/09/2026 - Hugo López Fernández
- 1.1.0 - 22/01/2024 - Hugo López Fernández
- 1.0.0 - 28/07/2023 - Hugo López Fernández
