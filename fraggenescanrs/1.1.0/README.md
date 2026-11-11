# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [FragGeneScanRs](https://github.com/unipept/FragGeneScanRs), a gene prediction tool.

# Using the FragGeneScanRs image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/fraggenescanrs FragGeneScanRs -s /data/seq_file.fas -o /data/out_name -w 1 -t complete`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `seq_file.fas` to the actual name of your FASTA file containing the DNA sequences that need to undergo gene prediction.
- `out_name` to the actual absolute path and prefix for the three output files (`out_name.out`, `out_name.faa` and `out_name.ffn`).
- `-w 1` indicates that the input has complete genomic sequences (use `-w 0` for short sequence reads).
- `-t complete` selects the training file; other options include `sanger_5`, `sanger_10`, `454_5`, `454_10`, `454_30`, `illumina_5` and `illumina_10`.

To see the [FragGeneScanRs](https://github.com/unipept/FragGeneScanRs) help, just run `docker run --rm pegi3s/fraggenescanrs --help`.
