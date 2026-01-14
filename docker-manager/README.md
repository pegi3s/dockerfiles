# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of docker-manager, a program with a graphical interface for managing Docker images.

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the `v1.2`, while users that did not yet update their Docker version to Docker 29 should use the image with the `v1.1` tag. Starting with version `v1.1.1-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

# Using the docker-manager image in Linux
You should run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp pegi3s/docker-manager`

Because of its graphical interface you must run the `xhost +` command first.
