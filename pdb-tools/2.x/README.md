# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PDB-tools](https://github.com/haddocking/pdb-tools), a swiss army knife for manipulating and editing PDB files.

# Using the PDB-tools image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pdb-tools bash -c <pdb-tool>`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<pdb-tool>` to the name of the `PDB-tool` you want to use.

For instance, in order to download the `1BRS` PDB structure, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/pdb-tools bash -c "pdb_fetch 1brs > 1brs.pdb"`

# Using the PDB-tools image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/pdb-tools bash -c <pdb-tool>`
