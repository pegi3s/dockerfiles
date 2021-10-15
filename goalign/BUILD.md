# Building instructions

Specify the goalign version in `goalign_version` and run:

```bash
goalign_version=0.3.5 && docker build ./ -t pegi3s/goalign:${goalign_version} --build-arg VERSION=${goalign_version}
```

# Build log

- 0.3.5 - 14/10/2021 - Hugo López Fernández
