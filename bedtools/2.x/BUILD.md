# Building instructions

Specify the bedtools version in `bedtools_version` and run:

```bash
bedtools_version=2.31.1 && docker build ./ -t pegi3s/bedtools:${bedtools_version} --build-arg VERSION=${bedtools_version}  && docker tag pegi3s/bedtools:${bedtools_version} pegi3s/bedtools:latest
```

# Build log

- 2.31.0 - 16/05/2023 - Hugo López Fernández
- 2.31.1 - 07/07/2026 - Hugo López Fernández
