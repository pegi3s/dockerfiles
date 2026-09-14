# Building instructions

Specify the ABySS version in `abyss_version` and run (from this `2.x/` directory).

## Default image (maximum k-mer length 192)

```bash
abyss_version=2.3.10 && docker build ./ -t pegi3s/abyss:${abyss_version} --build-arg VERSION=${abyss_version} && docker tag pegi3s/abyss:${abyss_version} pegi3s/abyss:latest
```

## Image with maximum k-mer length 256

```bash
abyss_version=2.3.10 && docker build ./ -t pegi3s/abyss:${abyss_version}-k.256 --build-arg VERSION=${abyss_version} --build-arg MAXK=256
```

# Notes

ABySS >= 2.3 requires [btllib](https://github.com/BirolLab/btllib), which is **not**
bundled in the ABySS release tarball (there is no btllib directory nor a git
submodule). This Dockerfile therefore builds btllib from its own release tarball
(`BTLLIB_VERSION`, default `1.7.8`) and passes `--with-btllib` to ABySS's configure.

The default maximum k-mer length (`--enable-maxk`) is 192 (the ABySS default). The
`-k.256` variant sets it to 256. The previous `-k.128` variant is no longer needed
since the default is now 192.

# Build log

- 2.3.10 - 14/09/2026 - Hugo López Fernández
