# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Minimap2](https://github.com/lh3/minimap2), a sequence read aligner.

# Using the Minimap2 image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data --entrypoint s pegi3s/minimap2 -c "minimap2 -a /data/chr_fastaFile /data/fastaFile > /data/output/aln.sam"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `chr_fastaFile` to the actual name of your reference genome in FASTA format.
- `fastaFile` to the actual name of your query sequences in FASTA or FASTQ format.
- `aln.sam` to the actual name of your output alignment file in SAM format.

To see the [Minimap2](https://lh3.github.io/minimap2/minimap2.html) help, just run `docker run --rm pegi3s/minimap2 --help`.
