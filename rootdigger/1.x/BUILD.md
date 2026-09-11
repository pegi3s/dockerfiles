# Building instructions

Specify the rootdigger version in `rootdigger_version` and run (from this `1.x/` directory):

```bash
rootdigger_version=1.8.0 && docker build ./ -t pegi3s/rootdigger:${rootdigger_version} --build-arg VERSION=${rootdigger_version}
```

This builds from the upstream release tag `v${VERSION}`. The resulting image is
**not** tagged as `latest`; the `latest` tag is reserved for the `master/`
(development) build.

# Notes

- The v1.8.0 source (coraxlib) links against `-lcblas`, which is provided by
  `libatlas-base-dev` on Ubuntu 22.04 (`libopenblas-dev` does not provide it).
  This directory therefore uses ATLAS, whereas `master/` uses OpenBLAS.
- At v1.8.0 `src/CMakeLists.txt` defines `RD_COMPILE_DEFS` but does not apply it
  to the target, so the built binary reports `GIT_REV` instead of the version.
  The build applies the upstream fix
  (`target_compile_definitions(rd PRIVATE ${RD_COMPILE_DEFS})`) before compiling.

# Build log

- 1.8.0 - 11/09/2026 - Hugo López Fernández
