

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/), a database with protein structure predictions for the human proteome and 20 other key organisms.

# Using the AlphaFold DB image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/alphafold_db bash -c "/opt/run /data/uniprotIDFile"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file with the [Uniprot ID](https://www.uniprot.org/)'s of all proteins for which a structure will be downloaded from the AlphaFold DB.  Additionally, this will be the same directory where a folder with the resulting structures will be created.
- `/uniprotIDFile` to the filename of the list of Uniprot ID's corresponding to the proteins that you want to obtain from AlphaFold.  Each line in the file should contain only one Uniprot ID.


# Using the AlphaFold DB image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/alphafold_db bash -c "/opt/run /data/uniprotIDFile"`