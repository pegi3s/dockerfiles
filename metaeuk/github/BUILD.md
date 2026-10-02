# Building instructions

Specify the MetaEuk version in `metaeuk_version` and run (from this `github/` directory):

```bash
metaeuk_version=7-bba0d80 && docker build ./ -t pegi3s/metaeuk:${metaeuk_version} --build-arg VERSION=${metaeuk_version} && docker tag pegi3s/metaeuk:${metaeuk_version} pegi3s/metaeuk:latest
```

# Notes

MetaEuk GitHub releases are named `<version>-<commit>` (e.g. `7-bba0d80`). This image
downloads the pre-compiled Linux binary for the SSE4.1 instruction set
(`metaeuk-linux-sse41.tar.gz`) from the GitHub release, so the build is pinned to a
given release tag.

# Build log

- 7-bba0d80 - 02/10/2026 - Hugo López Fernández
