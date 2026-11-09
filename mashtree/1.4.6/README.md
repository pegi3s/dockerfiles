# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Mashtree](https://github.com/lskatz/mashtree), a rapid comparison of whole genome sequence files.

# Using the Mashtree image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/mashtree --numcpus 12 --outtree /data/output/output.nwk /data/fastaFile1 /data/fastaFile2`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your FASTA files.
- `output.nwk` to the actual name of your output file.

To see the [Mashtree](https://github.com/lskatz/mashtree/tree/master/docs) help, just run `docker run --rm pegi3s/mashtree --help`.
