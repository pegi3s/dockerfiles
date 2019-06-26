# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HADDOCK](http://milou.science.uu.nl/services/HADDOCK2.2/) (High Ambiguity Driven biomolecular DOCKing) Prediction Server, an information-driven flexible docking approach for the modelling of biomolecular complexes.

# Using the HADDOCK Server image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/haddock_server bash -c "/opt/run"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input PDB folders with the input PDB files you want to analyze, as well as the input protein active and passive residues files.

For instance, each one of yours PDB (`PDB.*`) folders should have the following PDB (`*.pdb`) and residues files regarding Protein 1 and 2:

- `*.pdb1` -> Protein 1 PDB file
- `*.a1` -> Protein 1 Active Residues
- `*.p1` -> Protein 1 Passive Residues
- `*.pdb2` -> Protein 2 PDB file
- `*.a2` -> Protein 2 Active Residues
- `*.p2` -> Protein 2 Passive Residues

A zip file containing a simple example of input data can be found [here](https://drive.google.com/open?id=1ugJl07ZUriu_poy4AdZzpvjCtTrLS8CZ).

### *Note 1*
Please note that residues in files `*.a1`, `*.p1`, `*.a2`, `*.p2` must be listed in line 1 only. 

### *Note 2*

In order to be notified of the results you need to create a file called `parameters.haddock` filled with the following information:

`-F username="your_username" -F password="your_password"`

which must be in the same folder as the input folder. Registration can be done [here](https://nestor.science.uu.nl/auth/register/).

### *Note 3*

Don't forget to keep a delay between requests for at least 6 hours or your IP address could be banned.
For additional information please access `HADDOCK` manual [here](http://www.bonvinlab.org/software/haddock2.2/manual/).

### *Note 4*

For Developers: To see `Formfind` information, just run: `cat ./opt/info`.

# Using the HADDOCK Server image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/haddock_server bash -c "/opt/run"`
