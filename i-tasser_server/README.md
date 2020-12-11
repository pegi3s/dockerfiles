# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [I-TASSER](https://zhanglab.ccmb.med.umich.edu/I-TASSER/) (Iterative Threading ASSEmbly Refinement) Online Server, a hierarchical approach to protein structure prediction and structure-based function annotation.

# Using the I-TASSER Server image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/i-tasser_server bash -c "/opt/run /data/inputFolder /data/outputFolder"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input folder with the multi FASTA file with the residues you want to analyze, as well as a file with your I-TASSER account information. Additionally, this will be the same directory where a folder with the results will be created.
- `/inputFolder` to point to the folder that contains the multi FASTA file and the file with your I-TASSER access credentials (see `Note 2` further below).
- `/outputFolder` to point to the folder where the sub-folders with the results for each submitted job will be saved. For each sequence present in the input file you provided, a new folder will be created where these results will be.

### *Note 1*

You have the option to run the image without specifying the `/inputFolder` and the `/outputFolder`. If that is the case, this image will assume you have your input data in a folder named `/input` inside `/your/data/dir` and additionally will save the results in a new folder, named `/Results_I-TASSER`. For this, adapt and run the command:

`docker run --rm -v /your/data/dir:/data pegi3s/i-tasser_server bash -c "/opt/run"`

### *Note 2*

In order to successfully submit each job, you need to create a file called `parameters.itasser` filled with the following information:

`-F REPLY-E-MAIL="your_email_address" -F password="your_password"`

which must be in the same folder as your input FASTA file. Registration is mandatory for submission and can be done [here](https://zhanglab.ccmb.med.umich.edu/I-TASSER/registration.html).

### *Note 3*

For Developers: To see `Formfind information`, just run: `cat ./opt/info`.

# Using the I-TASSER Server image on Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command:
`docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/i-tasser_server bash -c "/opt/run /data/inputFolder /data/outputFolder"`