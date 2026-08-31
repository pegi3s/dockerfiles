# tagada 2.x

## Image versioning policy

Only the **Nextflow environment** (Java + Nextflow) is baked into this image.
The actual TAGADA pipeline version is **not** installed at build time — it is
specified by the user at runtime via the `-revision` argument to `nextflow run`,
for example:

```
nextflow run FAANG/analysis-TAGADA -revision 2.2.1 ...
```

Because the image content is independent of the TAGADA release, the image does
**not** need to be rebuilt when a new TAGADA version is published. Instead, the
existing image is simply **retagged** with the new version. A full rebuild is
only required when the Nextflow environment itself must be updated (e.g. a new
Nextflow version or a new `pegi3s/docker` base).

The base image is pinned (`FROM pegi3s/docker:29.0.1`) to ensure reproducibility.

## Retag command (use for new TAGADA releases)

```bash
tagada_version=2.2.1 && docker tag pegi3s/tagada:2.1.4-docker29.0.1 pegi3s/tagada:${tagada_version} && docker tag pegi3s/tagada:${tagada_version} pegi3s/tagada:latest
```

## Full rebuild command (only when Nextflow environment must change)

Run from this directory (`tagada/2.x/`):

```bash
tagada_version=2.2.1 && docker build ./ -t pegi3s/tagada:${tagada_version} && docker tag pegi3s/tagada:${tagada_version} pegi3s/tagada:latest
```

## Build log

- 2.2.1 - 31/08/2026 - Hugo Lopez Fernandez (retagged from 2.1.4-docker29.0.1)
- 2.1.4-docker29.0.1 - 09/01/2026 - Hugo Lopez Fernandez
