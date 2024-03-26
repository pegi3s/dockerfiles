# Building instructions

Specify the biopython version in `biopython_version` and run:

```bash
biopython_version=1.83 && docker build ./ -t pegi3s/biopython:${biopython_version} --build-arg VERSION=${biopython_version}  && docker tag pegi3s/biopython:${biopython_version} pegi3s/biopython:latest
