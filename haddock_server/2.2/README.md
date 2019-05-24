# Using the HADDOCK image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/haddock_server bash -c "/opt/run"`

Create a file called `parameters.haddock` filled with the following information:

`-F username="" -F password=""`

that must be in the same folder as the data folders.

The data folders must be of the format `PDB.*`