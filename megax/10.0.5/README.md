# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the MEGA X image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority --device /dev/dri/ -v "/your/data/dir:/data" pegi3s/megax megax`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `MEGA X`. 

Running this command opens the [MEGA X](https://www.megasoftware.net) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

*Note:* You may notice an error when executing the command that runs `MEGA X` Graphical User Interface due to an incompatibility between `Ubuntu 18.04` and `Chromium` browser. `MEGA X`funcionalities are not affected as well as the data will not be compromised.