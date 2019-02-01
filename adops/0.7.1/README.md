# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the ADOPS image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command:

- `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/adops-gui bash`

Once inside the container execute:

- `/opt/ADOPS/run.sh`

In the first command, you should replace:

- `/your/data/dir` to point to the directory that you want to have available at `ADOPS`.

Running this command opens the [ADOPS](http://sing-group.org/ADOPS/) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

If the `ADOPS` Graphical User Interface doesn't open, try running `xhost +` before the first command.