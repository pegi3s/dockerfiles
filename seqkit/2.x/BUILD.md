# Building instructions

Specify the seqkit version in `seqkit_version` and run:

```bash
seqkit_version=2.2.0 && docker build ./ -t pegi3s/seqkit:${seqkit_version} --build-arg VERSION=${seqkit_version}  && docker tag pegi3s/seqkit:${seqkit_version} pegi3s/seqkit:latest
```

# Build log

- 2.0.0 - 21/09/2021 - Hugo López Fernández
- 2.1.0 - 02/12/2021 - Hugo López Fernández
- 2.2.0 - 18/03/2022 - Hugo López Fernández
