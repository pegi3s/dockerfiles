# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the use of the [FastRoot](https://github.com/uym2/MinVar-Rooting) software aimed at rooting phylogenetic trees.

# Using the FastRoot image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/fastroot -i /data/input -m <method> -o /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to analyze.
- `input` to the actual name of your Newick input file.
- `<method>` to either MP (midpoint), MV (minVAR), OG (outgroup), or RTT (root-to-tip). If using OG, the -g option can be used to specify the outgroups. If more than one put them between quotes
- `output` to the actual name of your Newick output file.

To see the FastRoot help, just run `docker run --rm pegi3s/fastroot -h`.

# Using the FastRoot image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/fastroot -i /data/input -m <method> -o /data/output <options>`
