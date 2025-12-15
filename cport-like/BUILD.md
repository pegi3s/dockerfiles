# Building instructions

Run:

```bash
CPORT_LIKE_VERSION=2025.12 && docker build ./ -t pegi3s/cport-like:${CPORT_LIKE_VERSION} && docker tag pegi3s/cport-like:${CPORT_LIKE_VERSION} pegi3s/cport-like
```

# Build log

- 2023.11 - 30/11/2023 - Jorge Vieira
- 2024.05 - 21/05/2024 - Hugo López Fernández
- 2025.12 - 10/12/2025 - Jorge Vieira - added the possibility to easily change urls when building Docker image
