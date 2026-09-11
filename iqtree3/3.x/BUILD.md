# Building instructions

Specify the iqtree3 version in `iqtree3_version` and run:

```bash
iqtree3_version=3.1.4 && docker build ./ -t pegi3s/iqtree3:${iqtree3_version} --build-arg VERSION=${iqtree3_version} && docker tag pegi3s/iqtree3:${iqtree3_version} pegi3s/iqtree3:latest
```

# Build log

- 3.1.4 - 11/09/2026 - Hugo López Fernández
- 3.1.0 - 22/04/2026 - Hugo López Fernández
