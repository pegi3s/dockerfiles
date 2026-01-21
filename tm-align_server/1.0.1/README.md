# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TM-align](https://zhanglab.ccmb.med.umich.edu/TM-align/) Online Server, an algorithm for sequence independent protein structure comparisons.

# Using the TM-align Server image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/tm-align_server bash -c "/opt/run /data/inputFolder /data/outputFolder"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input folder with the two protein structures you want to analyze, in PDB format (`*.pdb`). Additionally, this will be the same directory where a folder with the results will be created.
- `/inputFolder` to point to the folder that contains both protein structures.
- `/outputFolder` to point to the folder where the results will be saved.

### *Note 1*

You have the option to run the image without specifying the `/inputFolder` and the `/outputFolder`. If that is the case, this image will assume you have your input data in a folder named `/input` inside `/your/data/dir` and additionally will save the results in a new folder, named `/Results_TM-align`. For this, adapt and run the command:

`docker run --rm -v /your/data/dir:/data pegi3s/tm-align_server bash -c "/opt/run"`


### *Note 2*

For Developers: To see `Formfind information`, just run: `cat ./opt/info`.

# Using the TM-align Server image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/tm-align_server bash -c "/opt/run /data/inputFolder /data/outputFolder"`
