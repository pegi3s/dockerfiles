# Building instructions

Specify the VCFtools version in `vcftools_version` and run:

```bash
vcftools_version=0.1.17 && docker build ./ -t pegi3s/vcftools:${vcftools_version} --build-arg VERSION=${vcftools_version} && docker tag pegi3s/vcftools:${vcftools_version} pegi3s/vcftools:latest
```

# Build log

- 0.1.17 - 20/07/2026 - Hugo López Fernandez
