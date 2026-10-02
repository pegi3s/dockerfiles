# Building instructions

Specify the ASTER version in `aster_version` and run (from this `1.x/` directory):

```bash
aster_version=1.25 && docker build ./ -t pegi3s/aster:${aster_version} --build-arg VERSION=${aster_version} && docker tag pegi3s/aster:${aster_version} pegi3s/aster:latest
```

# Notes

ASTER is compiled from source (`make`). The Dockerfile downloads the source tarball for the
release tag `v${VERSION}` (instead of cloning the default branch) so that the build is pinned
to a given version.

# Build log

- 1.25 - 01/10/2026 - Hugo López Fernández
- 1.23 - 10/07/2025 - Hugo López Fernández
