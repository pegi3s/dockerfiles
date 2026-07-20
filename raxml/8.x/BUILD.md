# Building instructions

Specify the RAxML version in `raxml_version` and run:

```bash
raxml_version=8.2.13 && docker build ./ -t pegi3s/raxml:${raxml_version} --build-arg VERSION=${raxml_version} && docker tag pegi3s/raxml:${raxml_version} pegi3s/raxml:latest
```

# Build log

- 8.2.13 - 20/07/2026 - Hugo López Fernandez
