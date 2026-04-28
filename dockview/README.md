# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of Dockview, a utility for recording average, minimum, and maximum CPU and RAM resources of running Docker images.

> [!WARNING]
> This image runs Docker in Docker version 29, and thus is only compatible with Docker 29.

# Using the dockview image in Linux

In order to run Dockview, execute the following Docker command in the working directory:

```bash
docker run -v $PWD:/data -v /var/run/docker.sock:/var/run/docker.sock pegi3s/dockview -t 1 -o /data/output
```

Where `-t 1` means that sampling will be performed every five seconds and `output` is the name of the file where the output will be saved.

Please, note that in the case of Docker images that run other Docker images, the CPU and RAM usage of the different Docker images should be added.
