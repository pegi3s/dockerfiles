# Building instructions

Specify the Trinity version in `trinity_version` and run:

```bash
trinity_version=2.15.2 && docker build ./ -t pegi3s/trinity:${trinity_version} --build-arg VERSION=${trinity_version} && docker tag pegi3s/trinity:${trinity_version} pegi3s/trinity:latest
```

# Build log

- 2.15.2 - 24/08/2026 - Hugo López Fernandez
