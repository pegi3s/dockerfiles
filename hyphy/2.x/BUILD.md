# Building instructions

Specify the HyPhy version in `hyphy_version` and run (from this `2.x/` directory):

```bash
hyphy_version=2.5.101 && docker build ./ -t pegi3s/hyphy:${hyphy_version} --build-arg VERSION=${hyphy_version} && docker tag pegi3s/hyphy:${hyphy_version} pegi3s/hyphy:latest
```

# Notes

HyPhy is compiled from source with CMake (`cmake . && make -j install`) and requires
CMake >= 3.15 and GCC >= 9, hence the `ubuntu:24.04` base image.

Starting with HyPhy 2.5, the main executable is **`hyphy`** (it was `HYPHYMP` in older
versions) and analyses are run as `hyphy <analysis> --alignment <file> ...`.

The optional features are enabled: zlib, BLAS, libcurl, OpenMP and MPI (the latter
produces the additional `HYPHYMPI` executable). `make install` installs the `hyphy`
executable into `/usr/local/bin` and the HyPhy resources into `/usr/local/share/hyphy`.

# Build log

- 2.5.101 - 14/09/2026 - Hugo López Fernández
