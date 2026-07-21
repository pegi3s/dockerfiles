# Building instructions

Specify the FastTree version in `fasttree_version` and run:

```bash
fasttree_version=2.2.0 && docker build ./ -t pegi3s/fasttree:${fasttree_version} --build-arg VERSION=${fasttree_version} && docker tag pegi3s/fasttree:${fasttree_version} pegi3s/fasttree:latest
```

# Build log

- 2.2.0 - 21/07/2026 - Hugo López Fernandez
