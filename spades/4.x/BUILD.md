# Building instructions

Specify the SPAdes version in `spades_version` and run:

```bash
spades_version=4.3.0 && docker build ./ -t pegi3s/spades:${spades_version} --build-arg VERSION=${spades_version} && docker tag pegi3s/spades:${spades_version} pegi3s/spades:latest
```

# Build log

- 4.3.0 - 20/07/2026 - Hugo López Fernandez
