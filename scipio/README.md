

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Scipio](https://www.webscipio.org/webscipio/download_scipio), a tool that can be used to locate the regions coding for a query protein sequence in a DNA target sequence, and thus to determine exact gene structures and reverse translations.

# Using the scipio image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/scipio bash -c "./main Genome Proteins"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `Genome` to the name of the FASTA file containing the genome sequences.
- `Proteins` to the name of the FASTA file containing the protein sequences.

There are several options that can be used to control, for instance, the BLAT search. Please, check the Scipio Manual.
