 # Building instructions

Run:

```bash
CURRENT_VERSION=2.14.0 && docker build ./ -t pegi3s/blast:${CURRENT_VERSION} --build-arg VERSION=${CURRENT_VERSION} && docker tag pegi3s/blast:${CURRENT_VERSION} pegi3s/blast:latest
```

# Build log

- 2.14.0 - 08/05/2023 - Hugo López Fernández
