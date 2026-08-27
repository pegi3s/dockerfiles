# Building instructions

Specify the Picard version in `picard_version` and run:

```bash
picard_version=3.5.0 && docker build ./ -t pegi3s/picard:${picard_version} --build-arg VERSION=${picard_version} && docker tag pegi3s/picard:${picard_version} pegi3s/picard:latest
```

# Build log

- 3.5.0 - 27/08/2026 - Hugo López Fernandez