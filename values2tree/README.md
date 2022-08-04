# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of `values2tree`, a set of scripts to draw UPGMA trees using lists of values.

# Using the values2tree image in Linux

You should adapt and run the following command: `docker run -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/values2tree bash -c "<choice> /your/data/dir <directory>"`

In this command, you should replace:
- `/your/data/dir` (please note that it must be declared twice) to point to the directory that contains the folder with the input files.
- `choice` to the actual program choice: `run_UPGMA_tree` or `run_DrosEU_data`.
- `directory` to the actual name of the folder containing the files to be processed (i.e. a directory name that exists at `/your/data/dir`).

## `run_UPGMA_tree`

When using `run_UPGMA_tree` as the choice, the input text files must be in the following format:

```
population<SPACE>value (one set of values per line)
```

For instance:

```
POPA 1653.1234
POPB 1499.6789
POPC 1775.4322
```

A folder is created named `trees` that contains 3 files: 
- The matrix file (.meg) used to draw the UPGMA tree (values are calculated using the module of the difference between pairs of populations and four decimal cases).
- A newick file with the corresponding tree (.nwk).
- An image file (.png) showing the UPGMA tree. 

Trees are obtained using the `megax_cc` [Docker image](https://hub.docker.com/r/pegi3s/megax_cc) and the drawing with the `plottree` [Docker image](https://hub.docker.com/r/pegi3s/plottree).

Use the following commands to run this example:

```bash
mkdir files
echo -e 'POPA 1653.1234\nPOPB 1499.6789\nPOPC 1775.4322' > files/test.dat
docker run -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd):/data" pegi3s/values2tree bash -c "run_UPGMA_tree $(pwd) files"
```

## `run_DrosEU_data`

When using run_DrosEU_data as the choice, the input text files must be in the following format:

```
population<underscore>observer (one set of values per line)
```

Note that popultion and observer names cannot have underscores.

For instance:

```
Header
POPA_researcher1 1582.0107 more stuff
POPA_researcher2 1807.8322 more stuff
POPB_researcher1 1335.2363 more stuff
POPB_researcher2 1751.4598 more stuff
POPC_researcher1 2526.9088 more stuff
POPC_researcher2 2499.7430 more stuff
<SPACE>
Other stuff...
```

When running this option, a folder named `prep_files` will be also created containing the files (one file per observer) that are processed by `run_UPGMA_tree`.

Use the following commands to run this example:

```bash
mkdir files_DrosEU
echo -e 'Header\nPOPA_researcher1 1582.0107 more stuff\nPOPA_researcher2 1807.8322 more stuff\nPOPB_researcher1 1335.2363 more stuff\nPOPB_researcher2 1751.4598 more stuff\nPOPC_researcher1 2526.9088 more stuff\nPOPC_researcher2 2499.7430 more stuff' > files_DrosEU/test.dat
docker run -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd):/data" pegi3s/values2tree bash -c "run_DrosEU_data $(pwd) files_DrosEU"
```

# Using the values2tree image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually C:) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/var/run/docker.sock:/var/run/docker.sock" -v "/c/Users/User_name/dir/":/data pegi3s/values2tree bash -c "<choice> /your/data/dir <directory>"`
