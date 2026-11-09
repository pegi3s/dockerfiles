# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [CAFE](https://github.com/hahnlab/CAFE), a gene family evolution analysis tool.

# Using the CAFE image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/cafe /data/scriptFile`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `scriptFile` to the actual name of a file containing the CAFE commands to run (e.g. `load -i /data/familyFile`, `tree -i /data/treeFile`, `lambda -s`, `report`).

CAFE requires a binary phylogenetic tree with branch lengths in Newick format and a file with gene family sizes as inputs.
