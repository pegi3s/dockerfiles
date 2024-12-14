# Building instructions

Specify the HTSeq version in `htseq_version` and run:

```bash
htseq_version=2.0.9 && docker build ./ -t pegi3s/htseq:${htseq_version} --build-arg VERSION=${htseq_version}  && docker tag pegi3s/htseq:${htseq_version} pegi3s/htseq:latest
```

# Build log

- 2.0.9 - 14/12/2024 - Hugo López Fernández
