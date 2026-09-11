# Building instructions

Specify the prank-msa version in `prank_version` and run:

```bash
prank_version=251117 && docker build ./ -t pegi3s/prank-msa:${prank_version} --build-arg VERSION=${prank_version} && docker tag pegi3s/prank-msa:${prank_version} pegi3s/prank-msa:latest
```

# Notes

Starting with this build, the image installs the self-contained pre-compiled
binary bundle published in the GitHub release
(`prank.linux64.${VERSION}.tgz`) instead of compiling the tool from source.
This avoids the build toolchain (g++, make, git) and the system `mafft` and
`exonerate` dependencies, which are already bundled in the release archive.

The version used is the GitHub release tag (e.g. `251117`). Note that the
PRANK authors did not update the internal version string in the source code, so
running `prank -version` still reports `v.250331` even though the image is
built from release `v.251117`.

# Build log

- 251117 - 11/09/2026 - Hugo López Fernández
- 250331 - 22/06/2026 - Hugo López Fernández
