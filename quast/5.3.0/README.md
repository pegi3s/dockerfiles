# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [QUAST](https://github.com/ablab/quast), a genome assembly evaluation tool.

# Using the QUAST image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/quast /data/fastaFile -o /data/output/quast_output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your assembly FASTA file.
- `output/quast_output` to the actual name of your output directory.

To see the [QUAST](http://quast.sf.net/manual.html) help, just run `docker run --rm pegi3s/quast --help`.
