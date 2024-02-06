# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PROBCONSRNA](http://probcons.stanford.edu/), a sequence alignment tool for nucleotide and sequences (DNA and RNA). This is true even knowing that the program outputs the text "PROBCONS version 1.1 - align multiple protein sequences and print to standard output" since it reuses the PROBCONS software.

# Using PROBCONSRNA image in Linux

In order to use this image you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/probcons_nuc bash -c "probcons /data/sequences.fasta > /data/sequences_aligned.fasta"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `sequences.fasta` to the actual name of your nucleotide FASTA file.
- `sequences_aligned.fasta` to the actual name of your aligned FASTA file.

To see the PROBCONSRNA help, just run `docker run --rm pegi3s/probcons_nuc probcons`.

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

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/probcons_nuc bash -c "probcons /data/sequences.fasta > /data/sequences_aligned.fasta"`
