# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [DeepProSite](https://github.com/WeiLab-Biology/DeepProSite), a protein binding site prediction tool.

# Using the DeepProSite image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/deepprosite /data/pdbFile /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `pdbFile` to the actual name of your protein structure (PDB) file.
- `output` to the actual name of your output directory, where the `submission.csv` file will be written. A more readable version of the results, `submission_formatted.tsv`, with two columns (amino acid and binding probability, one residue per line), is also written to this directory, together with `deepprosite.log`, which contains the full DeepProSite console output.

Note that DeepProSite predicts binding sites from a protein structure, so the input must be a PDB file.

To see the [DeepProSite](https://github.com/WeiLab-Biology/DeepProSite) help, just run `docker run --rm pegi3s/deepprosite --help`.
