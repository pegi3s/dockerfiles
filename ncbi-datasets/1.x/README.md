# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [NCBI Datasets](https://github.com/ncbi/datasets) resource to easily gather data from across NCBI databases. 

It comes with two commands: `datasets` and `dataformat`. To obtain the help of them, you just need to run `docker run --rm pegi3s/ncbi-datasets datasets --help` or `docker run --rm pegi3s/ncbi-datasets dataformat --help`.

# Using the NCBI Datasets image in Linux

To use the applications, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/ncbi-datasets <command> <subcommand> <options>`.

In this command, you should replace:
- `/your/data/dir` to point to the directory where you may store downloaded data.
- `<command>` the main command to use (`datasets` or `dataformat`).
- `<subcommand>` the name of the specific subcommand to use.
- `<options>` the specific command and subcommand options.

For instance, the following command will download the gene with GeneID 672 into `gene_672.zip`: `docker run --rm -v /your/data/dir:/data pegi3s/ncbi-datasets datasets download gene gene-id 672 --filename /data/gene_672.zip`


# Using the NCBI Datasets image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/ncbi-datasets <command> <subcommand> <options>`
