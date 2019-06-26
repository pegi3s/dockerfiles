# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [SPPIDER](http://sppider.cchmc.org/) (Solvent accessibility based Protein-Protein Interface iDEntification and Recognition) Prediction Server, a protein interface recognition server.

# Using the SPPIDER Server image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/sppider bash -c "/opt/run"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input PDB files you want to analyze.

### *Note 1*

In order to be notified of the results you need to create a file called `parameters.sppider` filled with the following information:

`-F EMail="your_mail_address"` 

which must be in the same folder as the input data.

### *Note 2*

Don't forget to keep a delay between requests for at least 15 seconds or your IP address will be banned, so do not run this image multiple times.
For additional information please access `SPPIDER` manual [here](https://sppider.cchmc.org/sppider_doc.html#About).

### *Note 3*

For Developers: To see `Formfind` information, just run: `cat ./opt/info`.

# Using the SPPIDER Server image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/sppider bash -c "/opt/run"`