# Building instructions

Specify the SeqModeller version in `seqmodeller_version` and run:

```bash
seqmodeller_version=1.0.1 && docker build ./ -t pegi3s/seqmodeller:${seqmodeller_version} --build-arg VERSION=${seqmodeller_version} && docker tag pegi3s/seqmodeller:${seqmodeller_version} pegi3s/seqmodeller:latest
```

# Build log

- 1.0.1 - 07/07/2026 - Hugo López Fernández
