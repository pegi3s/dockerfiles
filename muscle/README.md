# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MUSCLE](https://www.drive5.com/muscle/), a sequence alignment tool.

# Using the muscle image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/muscle -in /data/sequences.fasta -out /data/sequences_aligned.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `sequences.fasta` to the actual name of your input file.
- `sequences_aligned.fasta` to the actual name of your aligned (output) file.
