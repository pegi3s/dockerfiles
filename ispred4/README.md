# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ispred4](https://ispred4.biocomp.unibo.it/ispred/default/index), ISPRED4 predicts protein-protein interaction interface residues from a protein structure chain in PDB format.

# Using the ispred4 image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/ispred4 /data/input.pdb --chain A --output /data/output.ispred4.csv`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input PDB file. The prediction results will be written to the same mounted directory.
- `input.pdb` to the actual name of your input protein structure file in PDB format.
- `output.ispred4.csv` to the actual name of your main ISPRED4 prediction CSV file. A second simplified file named `output.ispred4.interface_residues.csv` will also be generated.

To see the [ispred4]() help, just run:
`docker run --rm pegi3s/ispred4 --help`
