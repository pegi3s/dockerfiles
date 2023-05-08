# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the pss-3d image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pss-3d map /data/structure.pdb /data/pss /data/background`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `structure.pdb` to the actual name of your PDB file.
- `pss` to the actual name of your file containing the location of the positively selected amino acid sites (one per line, in the format chain name <space> site <space> B factor (color) value (0-99)).
- `background` to the actual name of your file containing the background color of each chain (one per line, in the format chain name <space> B factor (color) value (0-99)). If no background file is provided, the B factor is assumed to be zero.

This program produces a PDB file called `mapped.structure.pdb` that should be open with PyMOL (for instance using our [pegi3s/pymol Docker image](https://hub.docker.com/r/pegi3s/pymol)). After loading the PDB file, add the following (adapt to your needs) command line to the command line box: spectrum b, blue_white_red, minimum=0, maximum=99. If the background of chain A is set to 0, that of chain B to 50, and positively selected amino acid sites to 99, this would mean that chain A is shown in blue, chain B in white and positively selected amino acid sites in red.

# Test data

To test this image, the input files are available [here](https://github.com/pegi3s/dockerfiles/tree/master/pss-3d/test_data/). Go there and download the `7dk3.pdb` (SARS-CoV-2 S trimer, S-open), `pss` (from [this publication](https://doi.org/10.3390/v14071565)) and `background` files, put them in your `/your/data/dir` directory and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pss-3d map /data/7dk3.pdb /data/pss /data/background`

This command generates the `mapped.7dk3.pdb` file.

To see the results either run:

```
xhost +
docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority --device /dev/dri/ -v "/your/data/dir:/data" pegi3s/pymol pymol
```

Under File, choose Open /data/mapped.7dk3.pdb, and then run the following command line in the command line box:
```
spectrum b, blue_white_green_red, minimum=0, maximum=99
```
Chain A, B, and C will be painted in blue, white, and green, respectively, and positively selected amino acid sites will be labeled in red.

Or, alternatively, you can create in the working directory a file named `pymolrc` with the following commands:
```
load /data/mapped.7dk3.pdb
spectrum b, blue_white_green_red, minimum=0, maximum=99
```

And then run:
```
docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority --device /dev/dri/ -v "/your/data/dir:/data" pegi3s/pymol bash -c "cp /data/pymolrc ~/.pymolrc && pymol"
```

# Changelog

The `latest` tag contains always the most recent version.

## [1.0.0] - 08/05/2023
- Initial `pss-3d` image containing the `map` command.
