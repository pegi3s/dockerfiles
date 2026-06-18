# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TreeTime](https://github.com/neherlab/treetime), a maximum-likelihood phylodynamic analysis tool.

# Using the TreeTime image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/treetime ancestral --aln /data/fastaFile --tree /data/newickFile --outdir /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your FASTA alignment file.
- `newickFile` to the actual name of your Newick tree file.
- `/data/output` to the actual output directory name.

To see the [TreeTime](https://treetime.readthedocs.io/en/latest/) help, just run `docker run --rm pegi3s/treetime treetime -h`.
