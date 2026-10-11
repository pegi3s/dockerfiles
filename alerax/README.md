# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [AleRax](https://github.com/BenoitMorel/AleRax), a species tree inference and reconciliation tool.

# Using the AleRax image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/alerax -f /data/families.txt -s /data/species_tree.nwk -p /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `families.txt` to the actual name of your families file, which describes the gene trees (or alignments) of each gene family.
- `species_tree.nwk` to the actual name of your starting species tree file (or `Random`).
- `output` to the actual name of the output directory.

To see the [AleRax](https://github.com/BenoitMorel/AleRax/wiki) help, just run `docker run --rm pegi3s/alerax --help`.
