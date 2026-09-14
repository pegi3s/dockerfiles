# Building instructions

Specify the subread version in `feature-counts_version` and run (from this `2.x/` directory):

```bash
feature-counts_version=2.1.1 && docker build ./ -t pegi3s/feature-counts:${feature-counts_version} --build-arg VERSION=${feature-counts_version} && docker tag pegi3s/feature-counts:${feature-counts_version} pegi3s/feature-counts:latest
```

# Notes

`featureCounts` is part of the [Subread](https://subread.sourceforge.net/) package
(not the Bioconductor `Rsubread` R package). This image installs the pre-compiled,
statically linked `featureCounts` binary from the official SourceForge release
(`subread-${VERSION}-Linux-x86_64.tar.gz`), so the version no longer depends on the
Ubuntu release (the previous approach used `apt-get install subread`). Only the
`featureCounts` binary is extracted from the archive.

The full Subread suite (all binaries) is available in the `pegi3s/subread` image.
This `feature-counts` image is maintained for back-compatibility and only includes
the `featureCounts` program.

# Build log

- 2.1.1 - 11/09/2026 - Hugo López Fernández
- 2.0.0 - 20/10/2021 - Hugo López Fernández
