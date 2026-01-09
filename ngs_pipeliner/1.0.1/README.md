# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [NGS_pipeliner](./manual.md), a docker-based and easy to use program to develop pipelines (mainly for Next Generation Sequencing).

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
