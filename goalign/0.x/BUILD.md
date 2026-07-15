# Building instructions

Specify the goalign version in `goalign_version` and run:

```bash
goalign_version=0.4.0 && docker build ./ -t pegi3s/goalign:${goalign_version} --build-arg VERSION=${goalign_version} && docker tag pegi3s/goalign:${goalign_version} pegi3s/goalign:latest
```

# Build log

- 0.4.0 - 14/07/2026 - Hugo López Fernández
- 0.3.5 - 14/10/2021 - Hugo López Fernández
