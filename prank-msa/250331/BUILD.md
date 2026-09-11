# prank-msa 250331 — Historical Reference

This directory is kept for historical reference only. It contains the
Dockerfile used to build `pegi3s/prank-msa:250331`, which compiled PRANK from
source (`git clone` of the default branch followed by `make`) and installed the
system `mafft` and `exonerate` packages.

This build has been superseded by the parametrized image at `prank-msa/`
(top level), which installs the self-contained pre-compiled binary bundle from
the GitHub release. See `prank-msa/BUILD.md` for the current build
instructions.

## Original build command

```bash
docker build ./ -t pegi3s/prank-msa:250331
```

## Build log

- 250331 - 22/06/2026 - Hugo López Fernández
