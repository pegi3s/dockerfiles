# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [IQ-TREE 3](https://github.com/iqtree/iqtree3), IQ-TREE 3 is a fast and versatile phylogenetic inference software that performs maximum-likelihood tree reconstruction, automatic evolutionary model selection, branch support analysis, partitioned phylogenomic analyses, ancestral state reconstruction, topology tests, and several other downstream phylogenetic tasks.

# Using the IQ-TREE 3 image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/iqtree3 iqtree3 -s /data/your_alignment.fasta -m MFP -mtree --merit BIC -B 1000 -alrt 1000 --bnni --seed 1 --prefix /data/output_files/run1 -T AUTO`

In this command, you should replace:
- `/your/data/dir` with your actual working directory
- `your_alignment.fasta` with the actual name of your alignment file inside your working directory
- `output_files` with the actual name of the folder where you want the output files to be written
- `run1` with the prefix you want for the output files

NOTES:
- The output folder must already exist before running the command
- This command is a robust default setup that performs automatic model selection, tree inference, and branch support analysis. See the manual for details.

# Options used in the standard command

- `-m MFP`: perform extended ModelFinder model selection and then infer the tree under the best-fit model
- `-mtree`: perform a full tree search for every tested model during model selection
- `--merit BIC`: use BIC as the criterion to rank and choose the best model
- `-B 1000`: perform 1000 ultrafast bootstrap replicates
- `-alrt 1000`: perform 1000 SH-aLRT replicates
- `--bnni`: optimize bootstrap trees by NNI on bootstrap alignments to reduce inflated support values
- `--seed 1`: set a fixed random seed for reproducibility
- `--prefix /data/output_files/run1`: prefix for all output files
- `-T AUTO`: automatically detect and use the available CPU threads

# Other useful options

- `--seqtype <type>`: explicitly set the sequence type (`BIN`, `DNA`, `AA`, `NT2AA`, `CODON`, `MORPH`)
- `-t <file|PARS|RAND>`: specify a starting tree
- `-o <taxon[,taxon,...]>`: define outgroup taxon or taxa
- `-p <file>`: partition file for partitioned analyses
- `--redo`: redo both ModelFinder and tree search
- `--redo-tree`: keep ModelFinder result and redo only the tree search
- `--safe`: enable safe likelihood kernel to avoid numerical underflow
- `--mem <num[G|M|%]>`: limit RAM usage
- `--runs <num>`: number of independent runs
- `-v`: verbose mode
- `-h`: print the help text
- `-V`: show the current version number

## Additional usage examples

### Model selection only
`docker run --rm -v /your/data/dir:/data pegi3s/iqtree3 iqtree3 -s /data/your_alignment.fasta -m MF -mtree --merit BIC --prefix /data/output_files/modeltest -T AUTO`

### Use a fixed model instead of automatic model selection
`docker run --rm -v /your/data/dir:/data pegi3s/iqtree3 iqtree3 -s /data/your_alignment.fasta -m GTR+F+I+G4 --prefix /data/output_files/run1 -T AUTO`

### Partitioned analysis
`docker run --rm -v /your/data/dir:/data pegi3s/iqtree3 iqtree3 -s /data/concat_alignment.fasta -p /data/partitions.nex -m MFP+MERGE --merit BIC -B 1000 --seed 1 --prefix /data/output_files/run1 -T AUTO`

## Additional remarks
- A single alignment usually means one alignment analyzed under one overall model
- A partitioned phylogenomic analysis usually means a concatenated alignment split into multiple partitions, such as genes or codon positions
- For partitioned datasets, using `-p` with a partition file is generally more appropriate than treating the whole matrix as a single alignment
- If you want to inspect the ranking of tested models, check the `.model.gz` file
- If you want to inspect the final chosen model and fitted parameters, check the `.iqtree` file

To see the [IQ-TREE 3](https://github.com/iqtree/iqtree3) help, just run:
`docker run --rm pegi3s/iqtree3 iqtree3 -h`
