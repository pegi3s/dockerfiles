# Building instructions

Specify the seqkit version in `fastqc_version` and run:

```bash
fastqc_version=0.12.1 && docker build ./ -t pegi3s/fastqc:${fastqc_version} --build-arg VERSION=${fastqc_version}  && docker tag pegi3s/fastqc:${fastqc_version} pegi3s/fastqc:latest
```

# Build log

- 0.12.1 - 12/05/2023 - Hugo López Fernández
