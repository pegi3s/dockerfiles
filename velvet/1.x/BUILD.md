# Building instructions

Specify the Velvet version in `velvet_version` and run:

```bash
velvet_version=1.2.10 && docker build ./ -t pegi3s/velvet:${velvet_version} --build-arg VERSION=${velvet_version} && docker tag pegi3s/velvet:${velvet_version} pegi3s/velvet:latest
```

# Build log

- 1.2.10 - 21/07/2026 - Hugo López Fernandez
