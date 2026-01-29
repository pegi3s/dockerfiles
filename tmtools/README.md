# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [tmtools](https://github.com/jvkersch/tmtools), an algorithm for sequence independent protein structure comparisons.

# Using the tmtools image in Linux

You should adapt and run the following command: 
`docker run -v /your/data/dir:/data pegi3s/tmtools bash -c "python script.py /data/PDB1.pdb /data/PDB2.pdb > /data/output"`

In this command, you should replace:
- `/your/data/dir` to point to the directory where the two protein structures you want to analyze are located, in PDB format (`*.pdb`). Additionally, this will be the same directory where a folder with the results will be created.
- `PDB1.pdb` to point to the first PDB file.
- `PDB2.pdb` to point to the second PDB file.
- `output` to point to the folder where the results will be saved.
