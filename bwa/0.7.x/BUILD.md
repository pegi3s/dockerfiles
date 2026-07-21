# Building instructions

Specify the BWA version in `bwa_version` and run:

```bash
bwa_version=0.7.19 && docker build ./ -t pegi3s/bwa:${bwa_version} --build-arg VERSION=${bwa_version} && docker tag pegi3s/bwa:${bwa_version} pegi3s/bwa:latest
```

# Build log

- 0.7.19 - 20/07/2026 - Hugo López Fernandez
