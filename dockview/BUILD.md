# Building instructions

Run:

```bash
CURRENT_VERSION=1.0.0 && docker build ./ -t pegi3s/dockview:${CURRENT_VERSION} --build-arg dockview_version=${CURRENT_VERSION} && docker tag pegi3s/dockview:${CURRENT_VERSION} pegi3s/dockview:latest
```

# Build log

- 1.0.0 - 28/04/2026 - Hugo López Fernández
