# Building instructions

Specify the gotree version in `gotree_version` and run:

```bash
gotree_version=0.5.2 && docker build ./ -t pegi3s/gotree:${gotree_version} --build-arg VERSION=${gotree_version} && docker tag pegi3s/gotree:${gotree_version} pegi3s/gotree

# Build log

- 0.5.2 - 16/07/2026 - Hugo López Fernandez
- 0.5.1 - 14/07/2026 - Hugo López Fernández
