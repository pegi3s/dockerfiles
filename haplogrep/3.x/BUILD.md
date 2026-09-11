# Building instructions

Specify the haplogrep version in `haplogrep_version` and run (from this `3.x/` directory):

```bash
haplogrep_version=3.3.2 && docker build ./ -t pegi3s/haplogrep:${haplogrep_version} --build-arg VERSION=${haplogrep_version} && docker tag pegi3s/haplogrep:${haplogrep_version} pegi3s/haplogrep:latest
```

# Notes

The release asset format changed from `haplogrep3-${VERSION}-linux.zip` (3.2.1) to
`haplogrep3-${VERSION}-linux.tar.gz` (3.3.2), so it is downloaded and extracted
with `tar`. The bundle is installed under `/opt/haplogrep3` and exposed through
`PATH` (`ENTRYPOINT ["haplogrep3"]`).

During the build, the tool is run once so that the reference phylogenetic trees
configured in `haplogrep3.yaml` are installed into `/opt/haplogrep3/trees`. This
avoids downloading them on every container run, which would otherwise happen
because haplogrep3 uses an ephemeral cache when run with `--rm`.

# Build log

- 3.3.2 - 11/09/2026 - Hugo López Fernández
- 3.2.1 - 08/05/2024 - Hugo López Fernández
