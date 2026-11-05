# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PhyML](https://github.com/stephaneguindon/phyml), a program for maximum likelihood phylogenetic inference from nucleotide or amino-acid sequence alignments.

# Using the PhyML image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/phyml bash -c "phyml -i /data/nexusFile -d nt -b 0"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `nexusFile` to the actual name of your NEXUS alignment file.
- `nt` to `aa` if your alignment contains amino-acid sequences.
- `0` to the desired number of bootstrap replicates.

PhyML writes two output files in the current working directory:
- `<nexusFile>_phyml_tree.txt`: the inferred phylogenetic tree.
- `<nexusFile>_phyml_stats.txt`: the analysis statistics and likelihood values.

To see the [PhyML](https://github.com/stephaneguindon/phyml) help, just run `docker run --rm pegi3s/phyml phyml -h`.

# Test data

A small NEXUS alignment is available at `http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/input_test_data/phyml.zip`.
