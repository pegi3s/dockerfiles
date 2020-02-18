# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the PyMOL image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority --device /dev/dri/ -v "/your/data/dir:/data" pegi3s/pymol pymol`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `PyMOL`. 

Running this command opens the [PyMOL](https://pymolwiki.org/index.php/Main_Page) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

# Test data
To test the previous command, a Protein Data Bank (PDB) file is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/pymol/1.8.4.0/test_data/4ow0.pdb).