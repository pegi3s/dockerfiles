# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PDBFixer](https://github.com/openmm/pdbfixer), a PDB file fixing tool.

# Using the PDBFixer image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pdbfixer /data/input.pdb --output=/data/output/fixed.pdb`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `input.pdb` to the actual name of your input PDB file.
- `fixed.pdb` to the actual name of your output file.

To see the [PDBFixer](https://htmlpreview.github.io/?https://github.com/openmm/pdbfixer/blob/master/Manual.html) help, just run `docker run --rm pegi3s/pdbfixer --help`.
