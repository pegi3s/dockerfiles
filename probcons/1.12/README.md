# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PROBCONS](http://probcons.stanford.edu/), a sequence alignment tool.

# Using PROBCONS image in Linux

In order to use this image you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/probcons bash -c "probcons /data/sequences.fasta > /data/sequences_aligned.fasta"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `sequences.fasta` to the actual name of your FASTA file.
- `sequences_aligned.fasta` to the actual name of your aligned FASTA file.

To see the PROBCONS help, just run `docker run --rm pegi3s/probcons probcons`.

# Test data

To test the previous command, you can copy and paste the following sample data into the `sequences.fasta` file:
```
>Sequence1
AAAAAAAATTTTTTTT
>Sequence2
AAAAAATTTTTT
>Sequence3
AAAATTTT
```

# Using PROBCONS image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/probcons bash -c "probcons /data/sequences.fasta > /data/sequences_aligned.fasta"`
