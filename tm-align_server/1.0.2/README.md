# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TM-align](https://zhanggroup.org/TM-align/) Online Server, an algorithm for sequence independent protein structure comparisons.

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

There is a server limit regarding the size of the files that can be submiited to the server of about 1 MB. In this case, in order to still be able to use the server only the CA traces are submitted rather than the full atomic detail, and thus, the visualization in the html file will only show the CA trace. It should be noted that the TM-score/alignment computation itself is unaffected, as TM-align only ever uses CA coordinates for that.

### *Note 3*

For Developers: To see `Formfind information`, just run: `cat ./opt/info`.

