# Building instructions

Run:

```bash
docker build ./ -t pegi3s/r_annotationdbi:1.68.0 && docker tag pegi3s/r_annotationdbi:1.68.0 pegi3s/r_annotationdbi
```

The `Dockerfile` was created using the `r_builder` Docker [image](http://bdip.i3s.up.pt/container/r_builder) with:

```bash
docker run -u "$(id -u):$(id -g)" --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd):/data" -w /data pegi3s/r_builder generate_dockerfile.sh config.json --dry-run
```

# Build log

- 1.68.0 - 7/2/2024 - Hugo López Fernández