# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ALFATClust](https://github.com/phglab/ALFATClust), a biological sequence clustering tool with dynamic threshold.

# Using the ALFATClust image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/alfatclust alfatclust -i /data/fastaFile -o /data/output/output.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your input FASTA file.
- `output.txt` to the actual name of your output cluster file.

To see the [ALFATClust](https://github.com/phglab/ALFATClust) help, just run `docker run --rm pegi3s/alfatclust alfatclust -h`.
