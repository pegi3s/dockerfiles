# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [GeneRax](https://github.com/benoitmorel/generax), a gene and species tree inference tool.

# Using the GeneRax image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/generax -f /data/families.txt -s /data/species_tree.nwk -p /data/output --rec-model UndatedDL --strategy EVAL`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `families.txt` to the actual name of your families file.
- `species_tree.nwk` to the actual name of your starting species tree file.
- `output` to the actual name of the output directory.

To see the [GeneRax](https://github.com/BenoitMorel/GeneRax/wiki) help, just run `docker run --rm pegi3s/generax --help`.
