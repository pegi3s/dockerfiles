# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MUSCLE](https://github.com/rcedgar/muscle), a sequence alignment tool.

# Using the MUSCLE image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/muscle -align /data/sequences.fasta -output /data/sequences_aligned.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `sequences.fasta` to the actual name of your input file.
- `sequences_aligned.fasta` to the actual name of your aligned (output) file.

To see the MUSCLE help, just run `docker run --rm pegi3s/muscle`.

# Using the MUSCLE image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/muscle -align /data/sequences.fasta -output /data/sequences_aligned.fasta`
