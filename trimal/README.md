# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [trimAl](https://github.com/inab/trimal), a multiple sequence alignments trimming tool.

# Using the trimAl image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/trimal -in /data/fastaFile -out /data/out_name.fas -gt 0.8`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your input alignment (FASTA) file.
- `out_name.fas` to the actual name of the output directory and output file.

To see the [trimAl](https://trimal.readthedocs.io) help, just run `docker run --rm pegi3s/trimal -h`.
