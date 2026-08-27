# Building instructions

Specify the Trimmomatic version in `trimmomatic_version` and run:

```bash
trimmomatic_version=0.41 && docker build ./ -t pegi3s/trimmomatic:${trimmomatic_version} --build-arg VERSION=${trimmomatic_version} && docker tag pegi3s/trimmomatic:${trimmomatic_version} pegi3s/trimmomatic:latest
```

# Build log

- 0.41 - 27/08/2026 - Hugo López Fernandez