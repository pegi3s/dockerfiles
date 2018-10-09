# (Please note that the original software licenses still apply)

# Using the MAUVE image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/mauve`

In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at MAUVE.

If the above command fails, try running `xhost +` first. 

Running this command opens the [MAUVE](http://darlinglab.org/mauve/mauve.html) Graphical User Interface. Your data directory will be available through the file browser at `/data`.
