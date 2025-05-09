# Using our Docker images with Podman

[Podman](https://podman.io/) is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. In Podman, containers can either be run as root or in rootless mode and it is compatible with Docker images.

This guide demonstrates how to run Docker images from our *Bioinformatics Docker Images Project* using Podman. To do so, the [`pegi3s/alter`](https://hub.docker.com/r/pegi3s/alter) Docker image in the examples.

## 1. Pulling a Docker image

To pull a public Docker image from Docker Hub, you should run the following command:

```shell
podman pull docker.io/pegi3s/alter
```

## 2. Running GUI applications

To run a GUI application, you can simply run the following command (run `xhost +` first if it fail):

```shell
podman run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" docker.io/pegi3s/alter
```

Where `/your/data/dir` is the host directory with the data files that is available in the image at `/data`.

## 3. Running CLI commands

To run CLI commands, you should simply run the following command:

```shell
podman run --rm -v /your/data/dir:/data docker.io/pegi3s/alter -i /data/input.nexus -o /data/output.fasta -ia -of FASTA -oo Linux -op GENERAL
```

Where `/your/data/dir` is the host directory with the data files that is available in the image at `/data`. You can try the above command using [this NEXUS file](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/alter/1.3.4/test_data/input.nexus):

```shell
wget https://raw.githubusercontent.com/pegi3s/dockerfiles/master/alter/1.3.4/test_data/input.nexus && \
    podman run --rm -v $(pwd):/data docker.io/pegi3s/alter \
        -i /data/input.nexus -o /data/output.fasta -ia -of FASTA -oo Linux -op GENERAL
```
