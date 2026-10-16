# Building instructions

Specify the EDirect version (date format) in `entrez_direct_version` and run (from this `26.x/` directory):

```bash
entrez_direct_version=26.5.20261015 && docker build ./ -t pegi3s/entrez-direct:${entrez_direct_version} --build-arg VERSION=${entrez_direct_version} && docker tag pegi3s/entrez-direct:${entrez_direct_version} pegi3s/entrez-direct:latest
```

# Notes

EDirect is distributed as versioned archives under
`https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/<VERSION>/`. This Dockerfile
downloads the `edirect.tar.gz` archive and the precompiled `xtract`, `rchive` and `transmute`
Linux binaries for the requested version, instead of using the unversioned
`install-edirect.sh` script (which always installs the latest release).

# Build log

- 26.5.20261015 - 16/10/2026 - Hugo López Fernández
- 10.0.20180927 - 14/07/2020 - Hugo López Fernández
