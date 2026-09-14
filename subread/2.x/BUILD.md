# Building instructions

Specify the subread version in `subread_version` and run (from this `2.x/` directory):

```bash
subread_version=2.1.1 && docker build ./ -t pegi3s/subread:${subread_version} --build-arg VERSION=${subread_version} && docker tag pegi3s/subread:${subread_version} pegi3s/subread:latest
```

# Notes

This image installs the pre-compiled Linux binaries from the official SourceForge
release (`subread-${VERSION}-Linux-x86_64.tar.gz`). All the Subread programs are
included and available on the `PATH`: `subread-align`, `subread-buildindex`,
`subjunc`, `exactSNP`, `sublong`, `subindel`, `featureCounts` and the utilities
(`flattenGTF`, `genRandomReads`, `propmapped`, `qualityScores`, `removeDup`,
`repair`, `subread-fullscan`, `txUnique`, `detectionCall`).

The `feature-counts` image is also available; it is kept for back-compatibility
and only includes the `featureCounts` program.

# Build log

- 2.1.1 - 14/09/2026 - Hugo López Fernández
