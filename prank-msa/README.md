# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PRANK](https://github.com/ariloytynoja/prank-msa), a probabilistic multiple alignment program for DNA, codon and amino-acid sequences.

# Using the PRANK image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/prank-msa -d=/data/fastaFile -o=/data/output/output -F`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your input FASTA file.
- `output` to the desired prefix for the output files (output.best.fas will be created).

To see the [PRANK](https://ariloytynoja.github.io/prank-msa) help, just run `docker run --rm pegi3s/prank-msa -help`.
