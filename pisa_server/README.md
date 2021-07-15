

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PDBePISA](https://www.ebi.ac.uk/pdbe/pisa/) (Proteins, Interfaces, Structures and Assemblies) Server, an interactive tool for the exploration of macromolecular interfaces.

# Using the PISA Server image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/pisa_server bash -c "/opt/run /data/inputFolder /data/outputFolder"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input folder with all `PDB` files you want to analyse with PISA. Additionally, this will be the same directory where a folder with the results will be created.
- `/inputFolder` to point to the folder that contains the `PDB` files to analyse. 
- `/outputFolder` to point to the folder where the XML results for each submitted `PBD` will be saved. (See `Note 2`)


### *Note 1*

You have the option to run the image without specifying the `/inputFolder` and `/outputFolder`. If that is the case, this image will assume you have your input data in a folder named `/input` inside `/your/data/dir` and will save the results in a new folder, named `/Results_PISA`. For this, adapt and run the command:

`docker run --rm -v /your/data/dir:/data pegi3s/pisa_server bash -c "/opt/run"`


### *Note 2*

This image additionaly includes a script called [`pisa_xml_extract`](https://github.com/pegi3s/dockerfiles/blob/master/utilities/MANUAL.md#pisa_xml_extract), which extracts information regarding the number of interface residues and the interface area from XML files generated using [PDBePISA](https://www.ebi.ac.uk/pdbe/pisa/). Therefore, it can be of use after obtaining the XML results from the current image. `pisa_xml_extract` belongs to a set of utilities and scripts from the [`pegi3s/utilities`](https://github.com/pegi3s/dockerfiles/blob/master/utilities/MANUAL.md) docker image. It can be accessed in `/opt/pisa_xml_extract`.


# Using the PISA Server image on Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/pisa_server bash -c "/opt/run /data/inputFolder /data/outputFolder`
