# Building instructions

Specify the seqkit version in `seqkit_version` and run:

```bash
seqkit_version=2.0.0 && docker build -t pegi3s/seqkit:${seqkit_version} --build-arg VERSION=${seqkit_version} .
```
