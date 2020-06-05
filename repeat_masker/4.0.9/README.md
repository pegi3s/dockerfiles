# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [RepeatMasker](http://www.repeatmasker.org/), a program that screens DNA sequences for interspersed repeats and low complexity DNA sequences and masks them. When using `RepeatMasker`, sequence comparisons can be performed by several popular search engines but here, in order to have a light Docker image, we have implemented only `HMMER` and `RMBlast`. This image comes with a copy of `Dfam 3.1` library (a profile `HMM` library derived from `Repbase` sequences), but a custom library of consensus sequences in FASTA format can be provided (see below), although it can be used with `RMBlast` only, since `HMMER` is only intended for use with profile `Hidden Markov Model` databases (such as `Dfam`).

To see `RepeatMasker` help, just run:  `docker run --rm pegi3s/repeat_masker bash -c "RepeatMasker -help"`. You can use the option `-pa` to use more than one processor, `-e hmmer` to use `HMMER` rather than the default `RMBlast` search engine, and `-s` to perform a slow but more accurate search.

# Using the RepeatMasker image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/repeat_masker bash -c "RepeatMasker -species <species_name>  -s  /data/input"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to analyze.
- `<species_name>` to the actual name of the species in the `Dfam` library, for instance `drosophila`.
- `input ` to the actual name of your input FASTA file.

*Note*:
To run `RepeatMasker` with a custom library you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/repeat_masker bash -c "cp /data/library_input /usr/local/RepeatMasker/Libraries/library_input && cd /usr/local/RepeatMasker && ./add_lib && RepeatMasker -lib /usr/local/RepeatMasker/Libraries/library_input -s  /data/input"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to analyze.
- `library_input` to the actual name of the FASTA file containing a set of consensus sequences.
- `input ` to the actual name of your input FASTA file.

# Using the RepeatMasker image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/repeat_masker bash -c "RepeatMasker -species <species_name>  -s  /data/input"`
