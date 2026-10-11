# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [paf2chain](https://github.com/AndreaGuarracino/paf2chain), a tool for alignment format conversion.

# Using the paf2chain image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/paf2chain bash -c "paf2chain -i /data/pafFile > /data/output.chain"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `pafFile` to the actual name of your PAF file. It must contain CIGAR strings in the cg:Z: tag.
- `output.chain` to the actual name of your output file.

To see the [paf2chain](https://github.com/AndreaGuarracino/paf2chain) help, just run `docker run --rm pegi3s/paf2chain --help`.
