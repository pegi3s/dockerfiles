# Building instructions

Specify the seqtk version in `seqtk_version` and run:

```bash
seqtk_version=1.5 && docker build ./ -t pegi3s/seqtk:${seqtk_version} --build-arg VERSION=${seqtk_version}  && docker tag pegi3s/seqtk:${seqtk_version} pegi3s/seqtk:latest
```

# Build log

- 1.4 - 21/06/2023 - Hugo López Fernández
- 1.5 - 07/07/2026 - Hugo López Fernández
