# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Cactus](https://github.com/ComparativeGenomicsToolkit/cactus), a reference-free whole-genome aligner.

# Using the Cactus image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/cactus cactus --binariesMode local --batchSystem single_machine /data/jobStore /data/input_seqfile.txt /data/output.hal`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `input_seqfile.txt` to the actual name of your sequence file describing the genomes and their Newick tree.
- `output.hal` to the actual name of your output file in HAL format.
- `jobStore` to the name of the temporary working directory used by Toil.

To see the [Cactus](https://github.com/ComparativeGenomicsToolkit/cactus/blob/master/doc/progressive.md) help, just run `docker run --rm pegi3s/cactus cactus --help`.
