# (Please note that the original software licenses still apply)

# Using the BDBM image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/mnt/shared" -v "/your/repository/dir:/mnt/repository" pegi3s/bdbm`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `BDBM`. 
- `/your/repository/dir` to point to the directory where you want a repository to be created. 

Running this command opens the [BDBM](https://www.sing-group.org/BDBM/index.html) Graphical User Interface. Your results will be available in the specified repository.
