# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PLOTTREE](https://github.com/iBiology/plottree) software. `PLOTTREE` is a command line tool written in Python, building on top of `matplotlib` and `Biopython.Phylo` module. It is designed for quickly visualizing a phylogenetic tree via a single command in terminal.

# Using the PLOTTREE image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/plottree bash -c "plottree <plottree-arguments> /data/input.nwk -o /data/output"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the NEWICK file you want to analyze.
- `input.nwk` to the actual name of your input NEWICK file.
- `output` to the actual name of your output file.

For instance, in order to plot a tree with fontsize (`-s`): 20, width (`-w`): 20 and height (`-l`): 15, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/plottree bash -c "plottree -s 20 -w 20 -l 15 /data/tree_muscle.nwk -o /data/output"`

To see the `PLOTTREE` help, just run `docker run --rm pegi3s/plottree plottree -h`.

# Test data
To test the previous command, the input NEWICK file used is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/plottree/0.0.2/test_data/tree_muscle.nwk).

# Using the PLOTTREE image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/plottree bash -c "plottree <plottree-arguments> /data/input.nwk -o /data/output"`
