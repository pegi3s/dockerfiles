# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [FigTree](https://github.com/rambaut/figtree), a graphical viewer of phylogenetic trees and as program for producing publication-ready figures.

# Using the FigTree image in Linux

Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority --device /dev/dri/ -v "/your/data/dir:/data" pegi3s/figtree`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `FigTree`. 

Running this command opens the [FigTree](https://github.com/rambaut/figtree) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

## Execution notes

*Note 1:* You may notice an error when launching the application that says `Desktop API is not supported on current platform`. You can safely ignore it, the `FigTree` funcionalities are not affected as well as the data will not be compromised.
