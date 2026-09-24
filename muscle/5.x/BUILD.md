# Building instructions

Specify the MUSCLE version in `muscle_version` and run (from this `5.x/` directory):

```bash
muscle_version=5.3 && docker build ./ -t pegi3s/muscle:${muscle_version} --build-arg VERSION=${muscle_version} && docker tag pegi3s/muscle:${muscle_version} pegi3s/muscle:latest
```

# Notes

MUSCLE 5.x is a complete rewrite of MUSCLE 3.x, so the command line interface changed: the
program is now invoked as `muscle -align <input> -output <output>` (instead of
`muscle -in <input> -out <output>`). Starting with version 5.1, upstream distributes
pre-compiled, statically linked Linux binaries, so this image downloads the binary from the
GitHub release (no compilation needed) and uses `debian:13-slim` as base image.

# Build log

- 5.3 - 24/09/2026 - Hugo López Fernández
- 3.8.31 - 27/05/2024 - Hugo López Fernández
