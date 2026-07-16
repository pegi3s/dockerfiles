# Building instructions

Specify the SeqTUI version in `seqtui_version` and run:

```bash
seqtui_version=0.1.1 && docker build ./ -t pegi3s/seqtui:${seqtui_version} --build-arg VERSION=${seqtui_version}  && docker tag pegi3s/seqtui:${seqtui_version} pegi3s/seqtui:latest
```

# Build log

- 0.1.1 - 27/10/2025 - Hugo López Fernández
