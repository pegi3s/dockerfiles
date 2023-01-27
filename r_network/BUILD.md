# Building instructions

Run:

```bash
R_NETWORK_VERSION=_v2 && R_DATA_ANALYSIS_VERSION=4.1.1_v2 && docker build ./ -t pegi3s/r_network:${R_DATA_ANALYSIS_VERSION}${R_NETWORK_VERSION} --build-arg R_DATA_ANALYSIS_VERSION=${R_DATA_ANALYSIS_VERSION} && docker tag pegi3s/r_network:${R_DATA_ANALYSIS_VERSION}${R_NETWORK_VERSION} pegi3s/r_network:latest
```

# Build log

- 4.1.1_v2_v1 - 26/01/2023 - Hugo López Fernández
- 4.1.1_v2_v2 - 27/01/2023 - Hugo López Fernández
