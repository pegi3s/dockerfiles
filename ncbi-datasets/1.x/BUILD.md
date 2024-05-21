# Building instructions

Specify the release version in `datasets_version` and run:

```bash
datasets_version=16.12.1 && docker build ./ -t pegi3s/ncbi-datasets:${datasets_version} --build-arg VERSION=${datasets_version}  && docker tag pegi3s/ncbi-datasets:${datasets_version} pegi3s/ncbi-datasets:latest
```

# Build log

- 16.12.1 - 30/04/2024 - Hugo López Fernández
