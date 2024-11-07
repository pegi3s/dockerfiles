# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of [seqtk](https://github.com/lh3/seqtk), a fast and lightweight tool for processing sequences in the FASTA or FASTQ format.

To show the available commands, just run: `docker run --rm pegi3s/seqtk`.

To obtain the help of a command, you just need to run: `docker run --rm pegi3s/seqtk <seqtk-command>` (e.g. `docker run --rm pegi3s/seqtk split`)

# Using the seqtk image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/seqtk <seqtk-command> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- ` <seqtk-command>` to the name of the `seqtk` application you want to use.
- `<options>` with the specific options of the `seqtk` command. These options will include the input/output files, which should be referenced under `/data/`.

# Using the seqtk image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/seqtk <seqtk-command> <options>`
