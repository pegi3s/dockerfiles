# Building instructions

Specify the GATK version in `gatk_version` and run:

```bash
gatk_version=4.7.0.0 && docker build ./ -t pegi3s/gatk-4:${gatk_version} --build-arg VERSION=${gatk_version} && docker tag pegi3s/gatk-4:${gatk_version} pegi3s/gatk-4:latest
```

# Build log

- 4.7.0.0 - 25/08/2026 - Hugo López Fernandez