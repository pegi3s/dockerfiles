# Building instructions

Specify the Bowtie 1 version in `bowtie1_version` and run:

```bash
bowtie1_version=1.3.1 && docker build ./ -t pegi3s/bowtie1:${bowtie1_version} --build-arg VERSION=${bowtie1_version} && docker tag pegi3s/bowtie1:${bowtie1_version} pegi3s/bowtie1:latest
```

# Build log

- 1.3.1 - 14/07/2026 - Hugo López Fernández
