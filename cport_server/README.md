
# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [CPORT](https://alcazar.science.uu.nl/services/CPORT/) (Consensus Prediction Of interface Residues in Transient complexes) Server, an algorithm for the prediction of protein-protein interface residues.

# Using the CPORT Server image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/cport_server bash -c "/opt/run /data/inputFolder /data/outputFolder <protein_chain>"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input folder with all sub-folders for each protein you want to analyse with CPORT. Additionally, this will be the same directory where a folder with the results will be created.
- `/inputFolder` to point to the folder that contains the sub-folders for each protein structure to analyse. Each sub-folder should contain a `.pdb` file (and an optional [WHISCY](https://wenmr.science.uu.nl/whiscy/) alignment file. Please see `Note 2` further down) with the same name as the folder it is in. For instance, to run the analysis for `pdb_file.pdb` you should put it under `/your/data/dir/inputFolder/pdb_file/`. 
- `/outputFolder` to point to the folder where sub-folders with the results for each submitted structure will be saved.
- `<protein_chain>` to the name of the chain you want to use.


### *Note 1*

You have the option to run the image without specifying the `/inputFolder`, the `/outputFolder` and even the `<protein_chain>`. If that is the case, this image will assume you have your input data in a folder named `/input` inside `/your/data/dir` and will save the results in a new folder, named `/Results_CPORT`. Additionally, you can opt to leave `<protein_chain>` empty and the docker image will use chain `A` as default. For this, adapt and run the command:

`docker run --rm -v /your/data/dir:/data pegi3s/cport_server bash -c "/opt/run"`

### *Note 2*

If you have WHISCY predictions for the `.pdb` files you want to analyze you can simply add them into each intended sub-folder under `/data/inputFolder`, renaming them to the same name as your files with `.phylseq` extension. This alignment must be given in [PHYLIP format](http://scikit-bio.org/docs/0.2.3/generated/skbio.io.phylip.html).

For instance, to use the WHISCY prediction for `pdb_file.pdb`, you should put it inside the same directory but renaming it to `pdb_file.phylseq`.

### *Note 3*

For Developers: To see `Formfind information`, just run: `cat ./opt/info`.


# Using the CPORT Server image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/cport_server bash -c "/opt/run /data/inputFolder /data/outputFolder <protein_chain>"`
