# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Multiz](https://github.com/multiz/multiz), a multiple sequence alignment tool that aligns two sets of alignment blocks sharing a common reference sequence.

# Using the Multiz image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/multiz /data/mafFile1 /data/mafFile2 1 > out.maf`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `mafFile1` to the actual name of your first input MAF file.
- `mafFile2` to the actual name of your second input MAF file.
- `out.maf` to the actual name of your aligned MAF file.

To see the [Multiz](http://www.bx.psu.edu/miller_lab) help, just run `docker run --rm pegi3s/multiz`.
