# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [pesto](https://pesto.epfl.ch/), PeSTo predicts protein-protein interaction interface residues from protein structure files in PDB format using a geometric deep learning model.

# Using the pesto image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/app/input -v /your/data/dir/output:/app/output pegi3s/pesto`

In this command, you should replace:
- `/your/data/dir` (twice) to point to the directory that contains the PDB file to be processed and where a folder named output will be created with the application results.
