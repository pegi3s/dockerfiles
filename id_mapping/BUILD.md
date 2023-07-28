# Building instructions

Run:

```bash
CURRENT_VERSION=$(cat current.version) && docker build ./ -t pegi3s/id-mapping:${CURRENT_VERSION} --build-arg version=${CURRENT_VERSION} && docker tag pegi3s/id-mapping:${CURRENT_VERSION} pegi3s/id-mapping:latest
```

# Build log

- 1.0.0 - 28/07/2023 - Hugo López Fernández
