# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ScanNet](https://github.com/jertubiana/ScanNet), a protein binding site prediction tool.

# Using the ScanNet image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/scannet conda run --no-capture-output -n scannet python3 /usr/local/bin/main.py /data/pdbFile --noMSA --predictions_folder /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `pdbFile` to the actual name of your PDB file, PDB ID, or Uniprot ID (with optional _chain suffix).
- `output` to the actual name of your output directory.

To see the [ScanNet](https://www.nature.com/articles/s41592-022-01490-7) help, just run `docker run --rm pegi3s/scannet conda run --no-capture-output -n scannet python3 /usr/local/bin/main.py --help`.
