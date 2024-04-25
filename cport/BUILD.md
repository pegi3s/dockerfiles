# Building instructions

Specify the cport version in `cport_version` and commit in `cport_commit` run:

```bash
cport_version=2024.04.16 && cport_commit="1bcd83d276a5e066617949fd4b57e6585106636f" && docker build ./ -t pegi3s/cport:${cport_version} --build-arg COMMIT=${cport_commit}  && docker tag pegi3s/cport:${cport_version} pegi3s/cport:latest
```

# Build log