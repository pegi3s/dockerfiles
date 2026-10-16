# Building instructions

Specify the R Project version in `r_version` and run:

```bash
r_version=4.6.1 && docker build ./ -t pegi3s/r_project:${r_version} --build-arg VERSION=${r_version} && docker tag pegi3s/r_project:${r_version} pegi3s/r_project:latest
```

# Build log

- 4.6.1 - 16/10/2026 - Hugo López Fernández
- 4.6.0 - 08/09/2026 - Jorge Vieira
