# Building instructions

The tag version of the image is composed by the base Biopython version followed by the current utilities version. The base Biopython version must be also set as build argument for the `docker build` command:

```bash
docker build ./ -t pegi3s/biopython_utilities:1.78_0.2.0 --build-arg biopython_version=1.78
```

# Build log

- 1.78_0.2.0 - 18/11/2021 - Hugo López Fernández
