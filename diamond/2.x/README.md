# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [DIAMOND](https://github.com/bbuchfink/diamond) a sequence aligner for protein and translated DNA searches, designed for high performance analysis of big sequence data.

To list the main commands, simply run: `docker run --rm -it pegi3s/diamond`.

To obtain the help of a specific command, you just need to run: `docker run --rm -it pegi3s/diamond <command>` (e.g. `docker run --rm -it pegi3s/diamond makedb`)

# Using the DIAMOND image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/diamond <command> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<diamond>` to the name of the `DIAMOND` command you want to use.
- `<options>` with the specific options of the `DIAMOND` application. These options will include the input/output files, which should be referenced under `/data/`.

# Using the DIAMOND image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/diamond <command> <options>`
