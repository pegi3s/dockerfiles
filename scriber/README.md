# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [scriber](https://biomine2.cs.vcu.edu/servers/SCRIBER/), This image facilitates the usage of scriber, SCRIBER predicts protein-binding residues from a protein structure and chain.

# Using the scriber image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/scriber /data/input.pdb A --output /data/scriber_results.csv`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input PDB file
- `input.pdb` to the actual name of your input protein structure file in PDB format (the declared chain must be A).
- `scriber_results.csv` to the actual name of your SCRIBER prediction CSV file. A second simplified file named output.scriber.interface_residues.csv will also be generated.

To see the [scriber](https://biomine2.cs.vcu.edu/servers/SCRIBER/) help, just run:
`docker run --rm pegi3s/scriber --help`
