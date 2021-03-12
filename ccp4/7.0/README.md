
# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [CCP4](https://www.ccp4.ac.uk/) (Collaborative Computational Project No. 4), a Software suite for Macromolecular X-Ray Crystallography, using command line operations.

### *Note 1*

This docker image runs version `7.0` of `CCP4` and it assumes you accept the software [license](http://www.ccp4.ac.uk/download/licence.php?pkg=ccp4&os=src) stated in `/ccp4/conditions.txt`.

This and other builds are available in [this repository](http://devtools.fg.oisin.rc-harwell.ac.uk/nightly/7.0/).

# Using the CCP4 image in Linux

Although  can be used for a variety of operations, here we demonstrate its use to run [PISA](https://www.ebi.ac.uk/pdbe/pisa/) (Proteins, Interfaces, Structures and Assemblies).

For this purpose, you should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/ccp4 bash -c "/ccp4/bin/run data/inputFolder data/outputFolder"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input folder with all protein structures you want to analyze. Additionally, this will be the same directory where a folder with the results will be created.
- `/inputFolder` to point to the folder that contains the protein structures to analyze.
- `/outputFolder` to point to the folder where sub-folders with the results for each submitted structure will be saved, as well as the configuration file for `PISA`.


### *Note 2*

You have the option to run the image without specifying the `/inputFolder` and the `/outputFolder`. If that is the case, this image will assume you have your input data in a folder named `/input` inside `/your/data/dir` and will save the results in a new folder, named `/Results_CCP4-PISA`. For this, adapt and run the command:

`docker run --rm -v /your/data/dir:/data pegi3s/ccp4 bash -c "/ccp4/bin/run"`



### *Note 3*

To see other options available with `PISA` inside `CCP4`, just run: `pisa` inside the docker image.


# Using the CCP4 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/ccp4 bash -c "/opt/run /data/inputFolder /data/outputFolder"`

