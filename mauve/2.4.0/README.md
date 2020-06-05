# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Mauve](http://darlinglab.org/mauve/mauve.html), a system for constructing multiple genome alignments in the presence of large-scale evolutionary events such as rearrangement and inversion.

# Using the Mauve image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/mauve  bash -c "progressiveMauve --output=/data/output /data/input1 /data/input2"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `output` to the actual name of your output file.
- `input1` to the actual name of your first input genome file.
- `input2` to the actual name of your second input genome file.

# Running the Mauve GUI in Linux
This docker image can be also used to run the `Mauve` GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/mauve`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `Mauve`. 

Running this command opens the `Mauve` Graphical User Interface. Your data directory will be available through the file browser at `/data`.

# Using the Mauve image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/mauve  bash -c "progressiveMauve --output=/data/output /data/input1 /data/input2"`