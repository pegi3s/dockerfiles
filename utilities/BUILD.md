# Building instructions

Run:

```bash
CURRENT_UTILITIES_VERSION=0.22.2-docker29.0.1 && docker build ./ -t pegi3s/utilities:${CURRENT_UTILITIES_VERSION} --build-arg utilities_version=${CURRENT_UTILITIES_VERSION} && docker tag pegi3s/utilities:${CURRENT_UTILITIES_VERSION} pegi3s/utilities:latest
```

# Build log

- 0.18.0 - 04/11/2021 - Hugo López Fernández
- 0.18.1 - 04/11/2021 - Hugo López Fernández
- 0.19.0 - 18/11/2021 - Hugo López Fernández
- 0.19.1 - 22/12/2021 - Hugo López Fernández
- 0.20.0 - 29/12/2021 - Hugo López Fernández
- 0.21.0 - 17/02/2022 - Hugo López Fernández
- 0.21.1 - 18/03/2022 - Hugo López Fernández
- 0.21.2 - 09/09/2022 - Hugo López Fernández
- 0.22.0 - 14/09/2022 - Hugo López Fernández
- 0.22.2 - 14/09/2022 - Jorge Vieira
- 0.22.2-docker29.0.1 - 13/01/2026 - Hugo López Fernández
