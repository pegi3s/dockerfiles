# Building instructions

Specify the diamond version in `diamond_version` and run:

```bash
diamond_version=2.1.8 && docker build ./ -t pegi3s/diamond:${diamond_version} --build-arg VERSION=${diamond_version}  && docker tag pegi3s/diamond:${diamond_version} pegi3s/diamond:latest
```

# Build log

- 2.1.8 - 24/10/2023 - Hugo López Fernández
