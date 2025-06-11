# Building instructions

Run:

```bash
docker build ./ -t pegi3s/r_pathfindr:2.4.2 && docker tag pegi3s/r_pathfindr:2.4.2 pegi3s/r_rcpa
```

The `Dockerfile` was created using the `r_builder` Docker [image](http://bdip.i3s.up.pt/container/r_builder) with:

```bash
docker run -u "$(id -u):$(id -g)" --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd):/data" -w /data pegi3s/r_builder generate_dockerfile.sh config.json --dry-run
```

# Build log

- 2.4.2 - 17/2/2025 - Hugo López Fernández
