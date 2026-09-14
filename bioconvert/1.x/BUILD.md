# Building instructions

Specify the bioconvert version in `bioconvert_version` and run (from this `1.x/` directory):

```bash
bioconvert_version=1.2.0 && docker build ./ -t pegi3s/bioconvert:${bioconvert_version} --build-arg VERSION=${bioconvert_version} && docker tag pegi3s/bioconvert:${bioconvert_version} pegi3s/bioconvert:latest
```

# Notes

The GitHub tag for this release is `v1.12.0`, but the actual version declared by the
package is `1.2.0` (as published on PyPI and Bioconda), which is the version used here.

This image installs bioconvert from Bioconda, whose recipe declares all the required
external tools and Python dependencies (`samtools`, `bamtools`, `bcftools`, `bedtools`,
`bedops`, `goalign`, `gotree`, `picard-slim`, `deeptools`, `seqtk`, `seqkit`,
`sra-tools`, the UCSC tools, etc.), so no hand-maintained requirements lists are needed.

# Build log

- 1.2.0 - 14/09/2026 - Hugo López Fernández
