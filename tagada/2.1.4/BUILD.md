# tagada 2.1.4 — Historical Reference

This directory is kept for historical reference only. It contains the original
Dockerfile used to build `pegi3s/tagada:2.1.4`, which used an unpinned base
image (`FROM pegi3s/docker`).

## Why this directory is no longer active

This build was superseded by `tagada/2.1.4-docker29.0.1/` (now renamed
`tagada/2.x/`), which pins the base image to `FROM pegi3s/docker:29.0.1` for
reproducibility.

## Important: image versioning policy

The TAGADA version is **not** baked into this image. Only the Nextflow
environment (Java + Nextflow) is installed at build time. The actual TAGADA
pipeline version is specified by the user at runtime via the `-revision`
argument to `nextflow run`, for example:

```
nextflow run FAANG/analysis-TAGADA -revision 2.1.4 ...
```

This means the image does **not** need to be rebuilt when a new TAGADA release
is published — the image is simply retagged. See `tagada/2.x/BUILD.md` for the
current build and retag instructions.

## Original build command

```bash
docker build ./ -t pegi3s/tagada:2.1.4
```

## Build log

- 2.1.4 - Hugo Lopez Fernandez
