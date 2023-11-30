# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image uses the code that was available at https://github.com/haddocking/cport on the 16/06/2023, and that, at that time was still under development. The methods that reliably work are: ispred4, scriber, spidder and psiver. You can show the help associated to the cport code by running: `docker run pegi3s/cport-like cport -h`

# Using the cport-like image in Linux
To run the custom batch script that allows running in batch mode PDB files and get results in csv format, you should create a file named config in your working directory with the following information:

```
input_dir=
chain=
method=
```

For instance, if the files to be processed are in a directory named "PDB", you want to always analyze chain "A" and use only the sppider and scriber methods, your config file should look like this:

```
input_dir=PDB
chain=A
method="sppider scriber"
```

The available methods are (according to the comments on cport github page on the 16/06/2023): scriber, ispred4, sppider, cons_ppisp, meta_ppisp, predictprotein, psiver, csm_potential, and scannet.

Then you should adapt and run the following command:

You should adapt and run the following command: `docker run -v /your/data/dir:/data pegi3s/cport-like bash -c "./batch"`

In this command, you should replace:
- `/your/data/dir`  to point to the directory that contains the config file and the folder with the input files you want to analyze.

# Test data
To test the cport batch mode you can download files from [alphafold](https://alphafold.ebi.ac.uk/), for instance.


## Execution notes
*Note 1:* In batch mode, methods are run one by one and not all at the same time in order to make sure that a problem with one of the servers will not prevent the user from getting results from the other servers. By doing so, it also makes sure that there is a reasonable time gap between submissions to the same server.

*Note 2:* Since all the methods implemented in cport run in servers, and these can be turned off, or the way input files are provided, or results returned, changed, some of the methods may not work. Usually, the methods that work are: ispred4, scriber, spidder and psiver.
