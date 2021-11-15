# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html) (Phylogenetic Analysis by Maximum Likelihood), a package of programs for phylogenetic analyses of DNA or protein sequences using maximum likelihood.

# Using the PAML image in Linux
*Note*: Most programs in the `PAML` package have control files that specify the names of the sequence data file, the tree structure file, and models and options for the analysis. The default control files are `baseml.ctl` for `baseml` and `basemlg`, `codeml.ctl` for `codeml`, `pamp.ctl` for `pamp`, `mcmctree.ctl` for `mcmctree`. You must change these control files accordingly.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/paml /data/control_file`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `control_file` to the actual name of the control file you want to run.

For instance, to run the control file for `codeml` you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/paml /data/codeml.ctl`

# Using the PAML image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --user $(id -u):$(id -g) --rm -v "/c/Users/User_name/dir/":/data pegi3s/paml /data/control_file`