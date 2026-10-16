# Building instructions

Specify the FreeBayes version in `freebayes_version` and run (from this `1.x/` directory):

```bash
freebayes_version=1.3.10 && docker build ./ -t pegi3s/freebayes:${freebayes_version} --build-arg VERSION=${freebayes_version} && docker tag pegi3s/freebayes:${freebayes_version} pegi3s/freebayes:latest
```

# Notes

Upstream distributes a pre-compiled, statically linked Linux binary
(`freebayes-<VERSION>-linux-amd64-static.gz`) in the GitHub releases, so this image downloads
the binary from the release tagged `v${VERSION}` (no compilation needed) and uses
`debian:13-slim` as base image. The `rCRS.fasta` reference (and its index) is bundled in the
image and copied to the working directory, so it can be used directly as `-f rCRS.fasta`.

# Build log

- 1.3.10 - 16/10/2026 - Hugo López Fernández
- 1.3.6 - 08/05/2024 - Hugo López Fernández
