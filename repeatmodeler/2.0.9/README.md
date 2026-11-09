# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [RepeatModeler](https://github.com/Dfam-consortium/RepeatModeler), a de novo repeat modeling tool.

# Using the RepeatModeler image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/repeatmodeler bash -c "BuildDatabase -name repeatmodeler_db /data/<fastaFile> && RepeatModeler -database repeatmodeler_db -threads 4"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `<fastaFile>` to the actual name of your input FASTA file.
- `repeatmodeler_db` to the actual name you want to give to the BLAST database created by `BuildDatabase`.
- `-threads 4` to the actual number of processors to use.

To see the RepeatModeler help, just run `docker run --rm pegi3s/repeatmodeler bash -c "RepeatModeler -h"`.
