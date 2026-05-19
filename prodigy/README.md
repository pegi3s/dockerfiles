# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PRODIGY](https://github.com/haddocking/prodigy), a binding affinity prediction tool for protein-protein complexes.

# Using the PRODIGY image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/prodigy /data/pdbFile`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file.
- `pdbFile` to the actual name of your PDB or mmCIF structure file.

To see the PRODIGY help, just run `docker run --rm pegi3s/prodigy -h`.
