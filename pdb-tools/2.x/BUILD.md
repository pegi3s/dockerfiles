# Building instructions

Specify the pdb-tools version in `pdb_tools_version` and run:

```bash
pdb_tools_version=2.7.0 && docker build ./ -t pegi3s/pdb-tools:${pdb_tools_version} --build-arg VERSION=${pdb_tools_version} && docker tag pegi3s/pdb-tools:${pdb_tools_version} pegi3s/pdb-tools:latest
```

# Build log

- 2.7.0 - 20/07/2026 - Hugo López Fernandez
