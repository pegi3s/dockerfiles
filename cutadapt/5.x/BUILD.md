# Building instructions

Specify the cutadapt version in `cutadapt_version` and run:

```bash
cutadapt_version=5.2 && docker build ./ -t pegi3s/cutadapt:${cutadapt_version} --build-arg VERSION=${cutadapt_version} && docker tag pegi3s/cutadapt:${cutadapt_version} pegi3s/cutadapt:latest
```

# Build log

- 5.2 - 16/07/2026 - Hugo López Fernandez
