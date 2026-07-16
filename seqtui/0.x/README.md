# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of [SeqTUI](https://github.com/ranwez-search/SeqTUI), a fast terminal-based viewer and command-line toolkit for molecular sequences (DNA, AA). View, translate, convert (to FASTA), and combine sequences aligned or not — all from the terminal. Key features include:

- Multi-format support: FASTA, PHYLIP, and NEXUS with auto-detection.
- NT to AA translation using 33 NCBI genetic codes.
- Concatenation and supermatrix construction.
- SNP extraction to VCF format.
- Interactive viewer with vim-style navigation.

To show the available options, run: `docker run --rm pegi3s/seqtui -h`.

# Using the SeqTUI image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/seqtui <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<options>` with the specific options of SeqTUI. These options will include the input/output files, which should be referenced under `/data/`.

For example, to convert a multi-line FASTA file to single-line FASTA: `docker run --rm -v /your/data/dir:/data pegi3s/seqtui /data/alignment.fasta -o /data/output/alignment_1L.fasta`

# Using the SeqTUI image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/seqtui <options>`
