# Building instructions

Root Digger does not publish formal releases with binaries, and the latest tag
(`v1.8.0`, 2022) is well behind the development branch. This directory builds
from a specific commit of the upstream `master` branch, pinned through the
`COMMIT` build argument for reproducibility. The resulting image is tagged with
the build date.

Specify the commit in `rootdigger_commit` and run (from this `master/` directory):

```bash
rootdigger_commit=315c718a0ba19767047ff6bfba61c5c0a24d494d && docker build ./ -t pegi3s/rootdigger:2026.09.11 --build-arg COMMIT=${rootdigger_commit} && docker tag pegi3s/rootdigger:2026.09.11 pegi3s/rootdigger:latest
```

# Build log

- 2026.09.11 (commit 315c718a) - 11/09/2026 - Hugo López Fernández
- master (unpinned) - 12/04/2023 - Hugo López Fernández
