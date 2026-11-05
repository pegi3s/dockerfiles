# Building instructions

Specify the PhyML version in `phyml_version` and run (from this `3.x/` directory):

```bash
phyml_version=3.3.20260528 && docker build ./ -t pegi3s/phyml:${phyml_version} --build-arg VERSION=${phyml_version} && docker tag pegi3s/phyml:${phyml_version} pegi3s/phyml:latest
```

# Notes

PhyML is fetched from the GitHub `v${VERSION}` tag and compiled from source
using autotools. `--disable-native` removes `-march=native`, so the resulting
binary is portable across CPUs.

# Build log

- 3.3.20260528 - 05/11/2026 - Hugo López Fernández
