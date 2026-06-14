# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Aclust](https://github.com/GarryGippert/Aclust), a sequence alignment and phylogenetic tree inference tool for protein sequences.

# Using the Aclust image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/aclust -s /opt/Aclust/dat/BLOSUM62.dat -p /data/output/aclust_out /data/fastaFile`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input FASTA file.
- `fastaFile` to the actual name of your input protein FASTA file.
- `aclust_out` to the actual name of your output prefix.

To see the [Aclust](https://github.com/GarryGippert/Aclust) help, just run `docker run --rm pegi3s/aclust -h`.
