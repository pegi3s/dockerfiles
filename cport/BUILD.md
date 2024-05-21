# Building instructions

Specify the cport version in `cport_version` run:

```bash
cport_version=2024.05 && cport_commit="a523b9cd70bf57dcd8d39a31185d03b53f76e493" &&  docker build ./ -t pegi3s/cport:${cport_version} --build-arg COMMIT=${cport_commit} && docker tag pegi3s/cport:${cport_version} pegi3s/cport:latest
```

# Build log

- 2024.05 - 21/05/2024 - Hugo López Fernández
