# Building instructions

Run:

```bash
docker build ./ -t pegi3s/metaeuk
```

# Notes

This old image downloaded MetaEuk from an unversioned URL
(`https://mmseqs.com/metaeuk/metaeuk-linux-sse41.tar.gz`), so it did not correspond to a
specific MetaEuk release. The `41.0.0` value recorded in the metadata was added later in bulk
and does **not** match any real MetaEuk version (MetaEuk releases are named `<number>-<commit>`;
the latest is `7-bba0d80`). The image built from this directory is therefore considered
unversioned / mislabeled as `41.0.0`.

# Build log

- unversioned (recorded as 41.0.0) - 21/12/2022 - Pedro Ferreira
