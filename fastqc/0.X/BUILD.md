# Building instructions

Specify the fastqc version in `fastqc_version` and run:

```bash
fastqc_version=0.13.0 && docker build ./ -t pegi3s/fastqc:${fastqc_version} --build-arg VERSION=${fastqc_version}  && docker tag pegi3s/fastqc:${fastqc_version} pegi3s/fastqc:latest
```

# Build log

- 0.13.0 - 08/10/2026 - Hugo López Fernández
- 0.12.1 - 12/05/2023 - Hugo López Fernández
