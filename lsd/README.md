# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the LSD image in Linux

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp pegi3s/lsd`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `LSD`.

Running this command opens the [LSD](https://github.com/nunofonseca/lineagesequencediscovery) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

## LSD GUI utilization notes

You can find a step-by-step tutorial [here](https://github.com/pegi3s/dockerfiles/blob/master/lsd/tutorial/README.md) showing how to use this image to find patterns. Nevertheless, it is important to note that:

1. To create a project in a different location than the default (e.g. `/data`), you must select `Other` in the `Folder to Create Project in:` option of the new session dialog. This will open a file selection dialog where you can find the `/data` directory.

![Project location](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/lsd/tutorial/3.png)

2. After finding patterns, a dialog to save them into a file will appear. In this dialog, you must save it with `.pat` extension. This way, LSD will be able to load it automatically. Otherwise, it won't be opened since LSD require the pattern files to end with `.pat`.

![Patterns file](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/lsd/tutorial/7.png)
