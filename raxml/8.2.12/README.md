# (Please note that the original software licenses still apply)

This images facilitates the usage of [RAxML](https://sco.h-its.org/exelixis/web/software/raxml/index.html) (Randomized Axelerated Maximum Likelihood), a program for sequential and parallel Maximum Likelihood based inference of large phylogenetic trees. It can also be used for post-analyses of sets of phylogenetic trees, analyses of alignments and, evolutionary placement of short reads.
It has originally been derived from `fastDNAml` which in turn was derived from Joe Felsentein's `dnaml` which is part of the `PHYLIP` package.

# Using the RAxML image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/raxml raxmlHPC <options> -w /data`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<options> ` with the specific  options. These options will include the input/output files, which should be referenced under `/data/`.
- `-w /data` to the actual name of the directory where output files will be created.

To test the previous command, you may follow the `Getting Started` section [here](https://sco.h-its.org/exelixis/web/software/raxml/hands_on.html).

For instance, to run a simple ML search on binary data, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/raxml raxmlHPC -m BINGAMMA -p 12345 -s /data/binary.phy -n T1 -w /data`

*Note*: You can view the resulting tree file using our [TreeView X](https://hub.docker.com/r/pegi3s/treeviewx/) docker image. 

To see `RAxML` help menu, you just need to run:  `docker run --rm pegi3s/raxml raxmlHPC -h`

# Using the RAxML image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/raxml raxmlHPC <options> -w /data`