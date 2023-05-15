# Building instructions

Specify the sratoolkit version in `sratoolkit_version` and run:

```bash
sratoolkit_version=3.0.5 && docker build ./ -t pegi3s/sratoolkit:${sratoolkit_version} --build-arg VERSION=${sratoolkit_version}  && docker tag pegi3s/sratoolkit:${sratoolkit_version} pegi3s/sratoolkit:latest
```

# Build log

- 3.0.5 - 15/05/2023 - Hugo López Fernández
- 3.0.1 - 31/01/2023 - Hugo López Fernández
