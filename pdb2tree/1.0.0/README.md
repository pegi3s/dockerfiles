# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of PDB2tree, an application that allows building an UPGMA ultrametric phylogram using structural dissimilarity (similarity according to TM-align scores).

# Using the PDB2tree image in Linux

You should adapt and run the following command: `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/pdb2tree`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the folder with the input files and the config file.

The config file must have the following fields:

```
dir=""
extra_dir=""
results_dir=""
HOST_DIR=""
```

where `dir` is the name of the folder containing the PDB files to be used, `extra_dir` is the name of the folder where intermediate files are saved, `results_dir` is the name of the folder where the Newick tree file, image, and summary will be saved, and `HOST_DIR` is the path to /your/data/dir.

UPGMA trees are obtained using mega_cc and the branch lengths are in units of 1 − largest TM-score.

