# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [pesto](https://pesto.epfl.ch/), PeSTo predicts protein-protein interaction interface residues from protein structure files in PDB format using a geometric deep learning model.

# Using the pesto image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/input/dir:/app/input -v /your/output/dir:/app/output pegi3s/pesto`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the local input directory containing one or more PDB files. The prediction results will be written to the mounted output directory.
- `input.pdb` to the actual name of your input protein structure file in PDB format. Multiple PDB files can be placed in the input directory.
- `interface_residues.csv` to the actual name of your CSV file containing residue-level interface predictions generated from the PeSTo output PDB files. The output directory also contains the predicted *_i0.pdb files.

To see the [pesto](https://github.com/LBM-EPFL/PeSTo) help, just run:
``
