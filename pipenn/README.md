# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [pipenn](https://github.com/ibivu/pipenn), PIPENN predicts protein-protein interaction interface residues from protein structure files using deep learning and protein sequence embeddings.

# Using the pipenn image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/pipenn /data/input.pdb /data/results`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the local directory containing the input PDB file. The prediction results will be written to the output directory specified in the command.
- `input.pdb` to the actual name of your input protein structure file in PDB format.
- `interface_residues.csv` to the actual name of your CSV file containing residue-level protein-protein interface prediction results. It is written inside the selected output directory.

To see the [pipenn](https://github.com/ibivu/pipenn) help, just run:
`docker run --rm pegi3s/pipenn`
