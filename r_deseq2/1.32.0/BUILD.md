# Building instructions

Run:

```bash
CURRENT_VERSION="1.32.0_v2" && docker build ./ -t pegi3s/r_deseq2:${CURRENT_VERSION} && docker tag pegi3s/r_deseq2:${CURRENT_VERSION} pegi3s/r_deseq2
```

# Build log

- 1.32.0 - 13/10/2021 - Hugo López Fernández
- 1.32.0_v1 - 24/02/2023 - Hugo López Fernández [just tagging existing 1.32.0 image]
- 1.32.0_v2 - 24/02/2023 - Hugo López Fernández
