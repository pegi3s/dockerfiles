# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image uses code from a project forked from another repository on GitHub. The original repository is located at https://github.com/haddocking/cport. We thank the team behind the original repository for their contribution to the community.
The code base is located at https://github.com/pegi3s/cport/.

You can show the help associated to the cport code by running:

```
docker run pegi3s/cport:latest cport -h
```

The tested methods are: scriber, ispred4, sppider, psiver and scannet.

# Using the cport image in Linux
To run script, you should adapt and run the following command: 

```
docker run -v /your/data/dir:/data -v /your/output/dir:/output pegi3s/cport:latest cport /data/<input_pdb_file> chain_id --pred method
```

In this command, you should replace:
- `/your/data/dir`  to point to the directory that contains the config file and the folder with the input files you want to analyze.
- `/your/output/dir` to point to the directory where the output files with the results will be saved. If the directory does not exist, it is created.
- `/data/<input_pdb_file>` to indicate the name of your input PDB file.
- `chain_id` to indicate the identifier of the chain you want to use.
- `--pred method` to indicates the method you want to use.

## Execution notes

*Note 1:* Since all the methods implemented in cport run in servers, and these can be turned off, or the way input files are provided, or results returned, changed, some of the methods may not work. Usually, the methods that work are: ispred4, scriber, spidder and psiver.