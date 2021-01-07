# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# List of utilities
This Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations. To show the help of a specific utility, run `docker run --rm pegi3s/utilities <utility_name> --help`.

The list of utilities is presented below, please refer to [this manual](https://github.com/pegi3s/dockerfiles/blob/master/utilities/MANUAL.md) for detailed instructions and examples.

- `backup_file`: creates a backup file of the file passed as parameter. By default, it adds the extension \".bak\" (or \".bak1\", \".bak2\", and so on, if a file with any of the previous extensions exist).
- `batch_fasta_remove_line_breaks`: removes the line breaks of sequences in one or more FASTA files.
- `batch_fasta_remove_stop_codons`: modifies the sequences in one or more FASTA files to remove the stop codons (TAA, TAG and TGA) at the end of sequences. Note that if the input files have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, stop codons will be removed from each sequence line.
- `check_multiple_3`: verifies if all sequences in a FASTA file are multiple of 3. If so, the exit code is 0. Otherwise, the exit code is 1. Note that the exit code can be captured with `$?`. Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, the script may produce unpredictable result.
- `deinterleave_fastq`: deinterleaves a FASTQ file of paired reads into two FASTQ files. Optionally, the output files can be compressed using GZip.
- `dockerhub_count_pulls`: lists the number of pulls of each image for a given Docker Hub user.
- `dockerhub_list_images_with_tags`: lists all the images and tags for a given Docker Hub user.
- `dockerhub_list_repo_with_tags`: lists the tags for a given Docker Hub repository (user/image).
- `fasta_put_headers_back`: replaces the sequence headers using the provided mapping file (with input headers in the first column and new headers in the second).
- `fasta_remove_line_breaks`: removes the line breaks of sequences in a FASTA file.
- `fasta_remove_sequences_with_in_frame_stops_or_n`: removes the sequences containing N's or in-frame STOP codons (TAA, TAG and TGA) and writes the output into a new file.
- `fasta_remove_stop_codons`: modifies the sequences in a FASTA file to remove the stop codons (TAA, TAG and TGA) at the end of sequences. Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, stop codons will be removed from each sequence line.
- `fasta_replace_and_save_headers`: replaces the sequence headers by correlative numbers starting at 1 with a specified prefix. Also, a headers map is created so that original sequence headers can be restored using the `fasta_put_headers_back` script. "echo -e" script.
- `fasta_reverse_complement`: reverses the sequences in a FASTA file and converts them into their complement counterparts. Also, a prefix can be added to the header of each sequence. Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. The scripts `fasta_complement` and `fasta_reverse` perform these two tasks separately.
- `fastq_to_fasta`: converts a FASTQ file into a FASTA file.
- `pipe_delimited_extractor`: extract sequences from FASTA files, according to the information in a given field, separated by pipes.
- `pisa_xml_extract`: extract information regarding the number of interface residues and the interface area from XML files generated using [PDBePISA](https://www.ebi.ac.uk/pdbe/pisa/).
- `rmlastline`: removes the last line of one or more files. Note that this command modifies the files passed as parameters.

# Changelog

The `latest` tag contains always the most recent version.

## [0.14.0] - 07/01/2021
- Add the `pipe_delimited_extractor` utility.

## [0.13.0] - 25/11/2020
- Add the `dockerhub_list_repo_with_tags`, `fasta_replace_and_save_headers`, `fasta_put_headers_back`, `fasta_complement`, `fasta_reverse`, `fasta_reverse_complement` utilities.
- Modify the `fasta_remove_line_breaks` to add a newline at the end of the output files.

## [0.12.0] - 24/11/2020
- Add the `pisa_xml_extract` utility.

## [0.11.0] - 31/10/2020
- Allow changing the tags of the Docker images used in the `fasta_remove_sequences_with_in_frame_stops_or_n` utility.

## [0.10.0] - 30/10/2020
- Add the `dockerhub_list_images_with_tags` utility.
- Rename `count_dockerhub_pulls` to `dockerhub_count_pulls`.

## [0.9.0] - 15/09/2020
- Add the `check_multiple_3` utility.

## [0.8.0] - 27/01/2020
- Add the `backup_file` utility.

## [0.7.0] - 24/01/2020
- Add the `fasta_remove_sequences_with_in_frame_stops_or_n` utility.

## [0.6.0] - 23/01/2020
- Add the `fasta_remove_stop_codons` and `batch_fasta_remove_stop_codons` utilities.

## [0.5.0] - 23/01/2020
- Add the `batch_fasta_remove_line_breaks` utility.

## [0.4.0] - 08/01/2020
- Add the `fasta_remove_line_breaks` utility.

## [0.3.0] - 06/11/2019
- Add the `count_dockerhub_pulls` utility.

## [0.2.0] - 11/05/2018
- Add the `fastq_to_fasta` utility.
- Add `--help` parameter to all utilities in order to show the usage instructions.

## [0.1.0] - 09/05/2018
- Initial `utilities` image containing the `rmlastline` and `deinterleave_fastq` utilities.
