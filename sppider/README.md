# Using the SPPIDER image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/sppider bash -c "/opt/run"`

Create a file called `parameters.sppider` filled with the following information:

`-F EMail="your_mail_address"`

that must be in the same folder as the data.

The data files must be of the format `*.pdb`

Don't forget to keep a delay between requests for at least 15 seconds or your IP address will be banned
(see https://sppider.cchmc.org/sppider_doc.html#About). 
For developers: to see formfind information: cat ./opt/info