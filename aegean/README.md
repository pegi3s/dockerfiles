# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MetaEuk](https://github.com/soedinglab/metaeuk), a modular toolkit designed for large-scale gene discovery and annotation in eukaryotic metagenomic contigs.

# Using the MetaEuk image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/metaeuk bash -c "module_name <options>"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `module_name` to the name of the module to be used.

An extended list of all `MetaEuk` modules can be obtained by running: `docker run --rm -v /your/data/dir:/data pegi3s/metaeuk bash -c "metaeuk -h"`

### *Note*

In order to run the [easy-predict workflow](https://github.com/soedinglab/metaeuk#easy-predict-workflow), that predicts proteins from contigs (fasta/db) based on similarities to targets (fasta/db) and returns FASTA and  GFF files, using FASTA files as input, you should run: `docker run -v /your/data/dir:/data pegi3s/metaeuk bash -c "metaeuk easy-predict contigsFasta proteinsFasta predsResults tempFolder"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `contigsFasta` to the FASTA files containing the genomic sequence to be annotated.
- `proteinsFasta` to the FASTA files containing the protein sequence to be used as reference. If multiple protein sequences are given, then one prediction will be made based on each protein sequence that is given.
- `predsResults` to the prefix that will be given to all output files.
- `tempFolder` to the name of the temporary folder that will be created for performing all calculations.

# Using the MetaEuk image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/metaeuk bash -c "module_name <options>"`