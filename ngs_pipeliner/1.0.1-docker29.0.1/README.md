# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [NGS_pipeliner](./manual.md), a docker-based and easy to use program to develop pipelines (mainly for Next Generation Sequencing).

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the version `1.0.1-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `1.0.1` tag. Starting with version `1.0.1-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

# Using the NGS-pipeliner image in Linux
You should adapt and run the following command:

```
docker run --rm -ti \
    -v /your_data_dir:/data \
    -e HOST_PATH=/your_data_dir \
    -e USERID=$UID \
    -e USER=$USER \
    -e DISPLAY=$DISPLAY \
    -v /var/db:/var/db:Z \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $HOME/.Xauthority:/home/developer/.Xauthority \
    -v /var/run/docker.sock:/var/run/docker.sock \
    pegi3s/ngs_pipeliner
```

In this command, you should replace:
- `/your/data/dir` to point to the directory in which you are going to create and execute your pipeline.

To see a more in depth explanation of how to use this tool or how to install it in a Windows machine take a look at the [NGS_pipeliner manual](./manual.md).
