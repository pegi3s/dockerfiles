# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the SeqModeller image in Linux

Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/seqmodeller`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `SeqModeller`.

Running this command opens the [SeqModeller](https://github.com/Dannyzimmer/SeqModeller) Graphical User Interface. SeqModeller is a powerful GUI application for generating synthetic DNA sequences with customizable patterns, insertions, and repeats. It is suitable for bioinformatics research, testing sequence analysis tools, and creating controlled datasets.

Your data directory will be available through the file browser at `/data`.
