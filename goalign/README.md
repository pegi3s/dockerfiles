# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of [Goalign](https://github.com/evolbioinfo/goalign), a set of command line tools to manipulate multiple alignments.

By running the command `docker run --rm pegi3s/goalign goalign help` you can list the commands included in Goalign.

To obtain the help of a particular application, you just need to run: `docker run --rm pegi3s/goalign goalign <goalign-application-name> -h` (e.g. `docker run --rm pegi3s/goalign goalign random -h`)

# Using the Goalign image in Linux

To run an application, you should adapt and run the following command: `docker run -v /your/data/dir:/data --rm pegi3s/goalign goalign <goalign-application-name> -i /data/input -o /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<goalign-application-name>` to the name of the `Goalign` application you want to use.
- `<input>` to the actual name of your input file.
- `out` to the actual name of your output file.

For instance, to use the `subseq` application, you should run: `docker run -v /your/data/dir:/data --rm pegi3s/goalign goalign subseq -i /data/align.fasta -s 2 -l 3 -o /data/align.sub.fasta`

A sample `align.fasta` file can be [this file](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/test_data/sequences.aligned.1.fasta): 

```
>Sequence1
AAAAAAAATTTTTTTT
>Sequence2
AAAAA-A-TTTTT-T-
>Sequence3
AAAAA-ATTTTTT-T-
``` 

# Using the Goalign image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/goalign goalign <goalign-application-name> -i /data/input -o /data/output`
