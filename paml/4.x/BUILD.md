# Building instructions

Specify the PAML version in `paml_version` and run:

```bash
paml_version=4.10.10 && docker build ./ -t pegi3s/paml:${paml_version} --build-arg VERSION=${paml_version} && docker tag pegi3s/paml:${paml_version} pegi3s/paml:latest
```

# Build log

- 4.10.10 - 20/07/2026 - Hugo López Fernandez
- 4.9j - 20/07/2026 - Hugo López Fernandez
- 4.9h - 15/11/2021 - Hugo López Fernández
- 4.9 - 10/04/2019 - pegi3S (Automated Docker Build)
