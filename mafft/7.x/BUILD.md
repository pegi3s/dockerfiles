# Building instructions

Specify the MAFFT version in `mafft_version` and run:

```bash
mafft_version=7.526 && docker build ./ -t pegi3s/mafft:${mafft_version} --build-arg VERSION=${mafft_version} && docker tag pegi3s/mafft:${mafft_version} pegi3s/mafft:latest
```

# Build log

- 7.526 - 26/08/2026 - Hugo López Fernandez
- 7.525 - 20/07/2026 - Hugo López Fernandez
- 7.505 - 17/10/2023 - Hugo López Fernández
