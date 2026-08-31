# splitstree 6.x

## Build command

```bash
splitstree_version=6.9.5 && docker build ./ -t pegi3s/splitstree:${splitstree_version} --build-arg VERSION=${splitstree_version} && docker tag pegi3s/splitstree:${splitstree_version} pegi3s/splitstree:latest
```

## Notes

Starting with version 6.9.x, the upstream installer script hosted at
`software-ab.cs.uni-tuebingen.de` is no longer published. This Dockerfile
downloads the self-contained Linux tarball from GitHub releases
(`SplitsTree-${VERSION}-linux-x86_64.tar.gz`), which bundles a JRE — no
system Java installation is required.

## Build log

- 6.9.5 - 31/08/2026 - Hugo Lopez Fernandez
