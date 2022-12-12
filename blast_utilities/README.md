# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# BLAST utilities

This Docker image contains scripts that may be useful when using [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi). 

# `blast_and_extract`

The `blast_and_extract` identifies and retrieves genome regions showing similarity to a protein.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities blast_and_extract <input_genome_FASTA> <reference_protein> <max_distance_hits> <extra_sequence> <evalue> <output_genome_regions>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process.
- `<input_genome_FASTA>` to the actual path of your input genome FASTA file.
- `<reference_protein>` to the actual path of your reference protein FASTA file.
- `<max_distance_hits>` to a number that specifies the maximum distance between BLAST hits to be considered the same region.
- `<extra_sequence>` to the number of nucleotides to be included 5' and 3' of the region retrieved in the BLAST search (2000 is suggested).
- `<evalue>` to the expectation value for `tblastn`.
- `<output_genome_regions>` to the actual name of your output file.

*Note*: the input/output files should be referenced under `/data/` (i.e. absolute paths must be used).

For instance, to run the script `blast_and_extract` using as arguments a nucleotide FASTA file named `genome.fasta`, a reference protein file named `protein.fasta`, 10000 bp for the maximum size between blast hits to be considered the same genome region, retrieve as well 2000 bp 5' and 3' of the region retrieved in the BLAST search, using an expect value of 0.05, and an output file named `genome_regions.fasta`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities blast_and_extract /data/genome.fasta /data/protein.fasta 10000 2000 0.05 /data/genome_regions.fasta`

# Test data

To test this utility, a nucleotide FASTA file (Drosophila melanogaster genome) and a protein FASTA file (darkener of apricot, isoform S) are available [here](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/blast_utilities/test-data-blast-and-extract.zip).

The command you should run in this case is: you should run: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities blast_and_extract /data/Drosophila.fasta /data/query.fasta 10000 2000 0.05 /data/genome_regions_3.fasta`

# `m3f1`

The `m3f1` gets multiple of three (3) coding sequences starting in frame one (1).

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities m3f1 <input_FASTA> <reference_protein> <result>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process.
- `<input_FASTA>` to the actual name of your input FASTA file.
- `<reference_protein>` to the actual name of your reference protein file.
- `<result>` to the actual name of your output file.

*Note*: the input/output files should be referenced under `/data/` (i.e. absolute paths must be used).

For instance, to run the script `m3f1` using as arguments a nucleotide FASTA file named `input.fasta`, a reference protein file named `protein.fasta` and an output file named `result`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities m3f1 /data/input.fasta /data/protein.fasta /data/result`

# Test data

To test this utility, the nucleotide FASTA file is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/blast_utilities/test_data/input.fasta) and the reference protein file is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/blast_utilities/test_data/protein.fasta).

# `2-way-blast`

`[DEPRECATED]`- This script is deprecated. Please use [pegi3s/two-way-blast](https://hub.docker.com/r/pegi3s/two-way-blast) Docker image instead, which runs the analysis faster by running tasks in parallel.

The `2-way-blast` performs a 2 way `BLAST` analysis.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities bash -c "2-way-blast <input_dir> <output_dir> <reference_nucleotide> <blast_type>"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process.
- `<input_dir>` to the actual name of your input directory.
- `<output_dir>` to the actual name of your output directory.
- `<reference_nucleotide>` to the actual name of your reference nucleotide file.
- `<blast_type>` to the name of either `blastn` or `tblastx` type of `BLAST` you want to use.

*Note*:  These input/output directories should be referenced under `/data/`.

For instance, to run the script `2-way-blast` with `tblastx` type and using as argument a folder with nucleotide FASTA files named `input`, an output folder named `output` and a reference nucleotide file named `nucleotide.fasta`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/blast_utilities bash -c "2-way-blast /data/input /data/output nucleotide.fasta tblastx"`

# Test data

To test this utility, the nucleotide FASTA files are available [here](https://github.com/pegi3s/dockerfiles/tree/master/blast_utilities/test_data/input) and the reference nucleotide file is available [here](https://github.com/pegi3s/dockerfiles/blob/master/blast_utilities/test_data/input/nucleotide.fasta).

# Changelog

The `latest` tag contains always the most recent version.

## [0.1.0] - 17/12/2019
- Initial `utilities` image containing the `m3f1` and `2-way-blast` utilities.

## [0.2.0] - 06/11/2020
- Updates the `m3f1` utility to show the values of the input parameters (useful for debugging purposes).
