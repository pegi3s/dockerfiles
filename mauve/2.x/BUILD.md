# Building instructions

Specify the Mauve version in `mauve_version` and run:

```bash
mauve_version=2.4.1 && docker build ./ -t pegi3s/mauve:${mauve_version} --build-arg VERSION=${mauve_version} && docker tag pegi3s/mauve:${mauve_version} pegi3s/mauve:latest
```

# Build log

- 2.4.1 - 21/07/2026 - Hugo López Fernandez
