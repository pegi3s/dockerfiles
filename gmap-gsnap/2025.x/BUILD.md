# Building instructions

Specify the GMAP-GSNAP version (date format) in `gmap_gsnap_version` and run (from this `2025.x/` directory):

```bash
gmap_gsnap_version=2025-07-31 && docker build ./ -t pegi3s/gmap-gsnap:${gmap_gsnap_version} --build-arg VERSION=${gmap_gsnap_version} && docker tag pegi3s/gmap-gsnap:${gmap_gsnap_version} pegi3s/gmap-gsnap:latest
```

# Notes

GMAP-GSNAP is compiled from source (`./configure && make && make install`). It requires a
C compiler and Perl. The `zlib1g-dev` and `libbz2-dev` packages are installed so that the
build enables support for gzip- and bzip2-compressed input files (auto-detected by
`configure`). Note that the download site is HTTP-only.

The original distribution site (http://research-pub.gene.com/gmap/) states that, as of
August 2026, it will no longer be maintained and that the source code is now distributed at
GitHub (https://github.com/Genentech/gmap-gsnap). The 2025-07-31 version used here is not yet
published as a GitHub release/tag (the latest GitHub tag is v2025-04-19), so the tarball is
still downloaded from the original site. When newer releases become available on GitHub, the
download URL should be updated accordingly.

# Build log

- 2025-07-31 - 14/09/2026 - Hugo López Fernández
