# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [JAligner](https://github.com/ahmedmoustafa/JAligner), a pairwise sequence alignment tool.

# Using the JAligner image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/jaligner /data/fastaFile1 /data/fastaFile2 EDNAFULL 10 1`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile1` to the actual name of your first input FASTA file.
- `fastaFile2` to the actual name of your second input FASTA file.
- `EDNAFULL` to the actual name of your scoring matrix (e.g. BLOSUM62 for proteins).
- `10` to the actual open gap penalty.
- `1` to the actual extend gap penalty.
