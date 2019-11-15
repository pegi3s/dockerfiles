# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# BLAST utilities
This Docker image contains scripts that may be useful when using [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi). 

# `m3f1`

The `m3f1` gets multiple of three (3) coding sequences starting in frame one (1).

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities m3f1 <input FASTA> <reference_protein> <result>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `<input FASTA>` to the actual name of your input FASTA file.
- `<reference_protein>` to the actual name of your reference protein file.
- `<result>` to the actual name of your output file.

*Note*:  These input/output files should be referenced under `/data/`.

For instance, to run the script `m3f1` using as arguments a nucleotide FASTA file named `input.fasta`, a reference protein file named `protein.fasta` and an output file named `result`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities m3f1 /data/input.fasta /data/protein.fasta /data/result`

# Test data

To test this utility, the nucleotide FASTA file is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/blast_utilities/test_data/input.fasta) and the reference protein file is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/blast_utilities/test_data/protein.fasta).
