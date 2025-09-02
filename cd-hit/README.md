#### Please, note that this repository only contains a mirror to the `biocontainers/cd-hit` Docker image, providing guidance on how to use it. This way, we can keep a copy of this Docker image in our account for the sake of repeatability. Read below for further information.

# cd-hit

The original Dockerfile is available at [DockerHub](https://hub.docker.com/r/biocontainers/cd-hit).

# Using the cd-hit image in Linux
You should adapt and run the following command:
`docker run -v /your/data/dir:/data pegi3s/cd-hit bash -c "cd-hit -i /data/input.fas -o /data/output -c 0.9"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fas` to the actual name of your input file with non-aligned sequences in fasta format.
- `output` to the actual name of the output file.
- -c is the sequence identity threshold, default is 0.9.


To see the [cd-hit](https://www.bioinformatics.org/cd-hit/) help, just run `docker run pegi3s/cd-hit bash -c "cd-hit -h"`.
