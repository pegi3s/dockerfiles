# Building instructions

Specify the MaxBin2 version in `maxbin2_version` and run:

```bash
maxbin2_version=2.2.7 && docker build ./ -t pegi3s/maxbin2:${maxbin2_version} --build-arg VERSION=${maxbin2_version} && docker tag pegi3s/maxbin2:${maxbin2_version} pegi3s/maxbin2:latest
```

# Build log

- 2.2.7 - 25/08/2026 - Hugo López Fernandez