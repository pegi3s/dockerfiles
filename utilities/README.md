# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# List of utilities
This Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations. To show the help of a specific utiliy, run `docker run --rm pegi3s/utilities <utility_name> --help`.

The list of utilities is presented below, please refer to [this manual](https://github.com/pegi3s/dockerfiles/blob/master/utilities/MANUAL.md) for detailed instructions and examples.

- `batch_fasta_remove_line_breaks`: removes the line breaks of sequences in one or more FASTA files.
- `count_dockerhub_pulls`: lists the number of pulls of each image for a given Docker Hub user.
- `deinterleave_fastq`: deinterleaves a FASTQ file of paired reads into two FASTQ files. Optionally, the output files can be compressed using GZip.
- `fasta_remove_line_breaks`: removes the line breaks of sequences in a FASTA file.
- `fastq_to_fasta`: converts a FASTQ file into a FASTA file.
- `rmlastline`: removes the last line of one or more files. Note that this command modifies the files passed as parameters.

# Changelog

The `latest` tag contains always the most recent version.

## [0.1.0] - 09/05/2018
- Initial `utilities` image containing the `rmlastline` and `deinterleave_fastq` utilities.

## [0.2.0] - 11/05/2018
- Add the `fastq_to_fasta` utility.
- Add `--help` parameter to all utilities in order to show the usage instructions.

## [0.3.0] - 6/11/2019
- Add the `count_dockerhub_pulls` utility.

## [0.4.0] - 8/01/2020
- Add the `fasta_remove_line_breaks` utility.

## [0.5.0] - 23/01/2020
- Add the `batch_fasta_remove_line_breaks` utility.
