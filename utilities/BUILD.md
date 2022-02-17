# Building instructions

Run:

```bash
CURRENT_UTILITIES_VERSION=0.21.0 && docker build ./ -t pegi3s/utilities:${CURRENT_UTILITIES_VERSION} --build-arg utilities_version=${CURRENT_UTILITIES_VERSION} && docker tag pegi3s/utilities:${CURRENT_UTILITIES_VERSION} pegi3s/utilities:latest
```

# Build log

- 0.18.0 - 04/11/2021 - Hugo López Fernández
- 0.18.1 - 04/11/2021 - Hugo López Fernández
- 0.19.0 - 18/11/2021 - Hugo López Fernández
- 0.19.1 - 22/12/2021 - Hugo López Fernández
- 0.20.0 - 29/12/2021 - Hugo López Fernández
- 0.21.0 - 17/02/2022 - Hugo López Fernández
