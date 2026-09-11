# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Root Digger](https://github.com/computations/root_digger), a program, that will, when given a multiple sequence alignment and an unrooted tree with branch lengths, place a root on the given tree.

To obtain the application help, you just need to run: `docker run --rm pegi3s/rootdigger rd --help`.

# Using the Root Digger image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/rootdigger rd --msa /data/sequences_aligned.fasta --tree /data/Newick_tree_file --mode`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `sequences_aligned.fasta` to the actual name of your aligned FASTA file.
- `Newick_tree_file` to the name of the Newick file containing the unrooted tree with branch lengths.
- `--mode` to either `--exhaustive` or `--early-stop`.

# Test data

To test the previous command, you can use the `Popset_2312465787.fas` and `Popset_2312465787.nwk` files [here](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/input_test_data/rootdigger.zip) provided, and, after replacing `/your/data/dir` by the actual working directory, run the following command:

```
docker run --rm -v /your/data/dir:/data pegi3s/rootdigger rd --msa /data/Popset_2312465787.fas --tree /data/Popset_2312465787.nwk --exhaustive
```

# Using the Root Digger image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/rootdigger rd --msa /data/sequences_aligned.fasta --tree /data/Newick_tree_file --mode`
