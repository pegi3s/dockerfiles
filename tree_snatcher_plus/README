# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the TreeSnatcher Plus image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp pegi3s/tree_snatcher_plus`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `TreeSnatcher Plus`. 

Running this command opens the [TreeSnatcher Plus](https://www.cs.hhu.de/en/research-groups/computational-cell-biology/software-contributions/treesnatcher) Graphical User Interface. Your data directory will be available through the file browser at `/data`.
