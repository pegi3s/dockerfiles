# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [FAMSA](https://github.com/refresh-bio/FAMSA), a multiple sequence alignment tool.

# Using the FAMSA image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/famsa /data/fastaFile /data/output.fas`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your input FASTA file.
- `output.fas` to the actual name of your aligned FASTA file.

To see the [FAMSA](https://github.com/refresh-bio/FAMSA) help, just run `docker run --rm pegi3s/famsa -help`.
