

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of getpdb, a script that facilitates the retrieval of PDB structures associated with a given UniProt number, from the [PDB database](https://www.rcsb.org/).

# Using the getpdb image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/getpdb bash -c "./getpdb UniProt_number"`

In this command, you should replace:
- `/your/data/dir` to point to the working directory, where the retrieved PDB files will be saved.
- `UniProt_number` to the UniProt number to be used. Only one UniProt number can be specified.

# Using the getpdb image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/getpdb bash -c "./getpdb UniProt_number"`
