# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [DIALIGN](https://bibiserv.cebitec.uni-bielefeld.de/dialign), a multiple sequence alignment program based on segment-to-segment comparison.

# Using the DIALIGN image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/dialign bash -c "./dialign2-2 -n /data/small_not_aligned.fas"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your FASTA sequence file.
- `small_not_aligned.fas` to the actual name of your input FASTA file containing nucleotide or protein sequences.

To see the [DIALIGN](https://bibiserv.cebitec.uni-bielefeld.de/dialign/) help, just run:
`docker run --rm pegi3s/dialign ./dialign2-2`
