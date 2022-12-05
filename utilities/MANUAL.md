# `pegi3s/utilities` manual

The `pegi3s/utilities` Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations. To show the help of a specific utility, run `docker run --rm pegi3s/utilities <utility_name> --help`.

   * [backup_file](#backup_file)
   * [batch_fasta_remove_line_breaks](#batch_fasta_remove_line_breaks)
   * [batch_fasta_remove_stop_codons](#batch_fasta_remove_stop_codons)
   * [check_multiple_3](#check_multiple_3)
   * [create_batches](#create_batches)
   * [create_batches_for_directory](#create_batches_for_directory)
   * [deinterleave_fastq](#deinterleave_fastq)
   * [dockerhub_count_pulls](#dockerhub_count_pulls)
   * [dockerhub_list_images_with_tags](#dockerhub_list_images_with_tags)
   * [dockerhub_list_repo_with_tags](#dockerhub_list_repo_with_tags)
   * [fasta_extract_accession_numbers](#fasta_extract_accession_numbers)
   * [fasta_pipe_delimited_extractor](#fasta_pipe_delimited_extractor)
   * [fasta_put_headers_back](#fasta_put_headers_back)
   * [fasta_remove_line_breaks](#fasta_remove_line_breaks)
   * [fasta_remove_sequences_with_in_frame_stops_or_n](#fasta_remove_sequences_with_in_frame_stops_or_n)
   * [fasta_remove_stop_codons](#fasta_remove_stop_codons)
   * [fasta_rename_headers_with_taxonomy_info](#fasta_rename_headers_with_taxonomy_info)
   * [fasta_replace_and_save_headers](#fasta_replace_and_save_headers)
   * [fasta_reverse_complement](#fasta_reverse_complement)
   * [fasta_sort_by_header](#fasta_sort_by_header)
   * [fastq_to_fasta](#fastq_to_fasta)
   * [get_phylo_taxa](#get_phylo_taxa)
   * [get_taxonomy](#get_taxonomy)
   * [hdock_to_PDBePISA_conversion](#hdock_to_PDBePISA_conversion)
   * [pisa_xml_extract](#pisa_xml_extract)
   * [rmlastline](#rmlastline)


## `backup_file`

The `backup_file` script creates a backup file of the file passed as parameter. By default, it adds the extension \".bak\" (or \".bak1\", \".bak2\", and so on, if a file with any of the previous extensions exist).

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities backup_file /data/file.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to backup.
- `file.txt` to the actual names of your input file.

This command will create a file named `/your/data/dir/file.txt.backup`. If this file already exist, the new backup file will be named `/your/data/dir/file.txt.backup.1`. Run the following commands to re-create this effect:

```bash
for i in {1..3}; do 
    touch /tmp/file.txt
    docker run --rm -v /tmp:/data pegi3s/utilities backup_file /data/file.txt
    echo -e "\nFiles after iteration $i":
    ls -1a /tmp/ | grep 'file.txt'
done
```

## `batch_fasta_remove_line_breaks`

The `batch_fasta_remove_line_breaks` script removes the line breaks of sequences in one or more FASTA files. This command will process all the input FASTA files specified, editing them in place and using the [`fasta_remove_line_breaks`](#fasta_remove_line_breaks) script for it.

When processing large FASTA files (> 2 000 000 sequences), this script requires Docker since it runs commands from other images (`pegi3s/seqkit`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /tmp:/tmp`: mounts the host's `/tmp` directory in the same path.
- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

Then, the path containing the input and output files can be mounted in the two ways explained below.

In case you need to specify the versions of the pegi3s Docker images to use, you can pass them as environment variables to the Docker command. Just add the following parameters to the commands explained below:

```
--env VERSION_SEQKIT=0.16.1
```

To test this utility, you can copy and paste the following sample data into the `input1.fasta` and `input2.fasta` files:
```
>1
GATGGAGCGAAAAGAAATGA
GTATCGTATGCCGTCTTCTG
CTTGAAAAA
>2
TTGGACGGGACGTGACGAAA
CGGTATCGTATGCCGTCTTC
TGCTTGAAATGCTTGAAACT
TGCTTGAAATGCTTGAAAAG
```

### Option 1 (recommended): mount the local absolute path into the docker container

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/your/data/dir pegi3s/utilities batch_fasta_remove_line_breaks /your/data/dir/input1.fasta /your/data/dir/input2.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input*.fasta` to the actual name of your input FASTA files.

Note that it is possible to use bash wildcards such as `/your/data/dir/*` when running the command, altough in this case the command should be called using `bash -c`, that is: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/your/data/dir pegi3s/utilities bash -c "batch_fasta_remove_line_breaks /your/data/dir/*.fasta"`

### Option 2: mount the host path as `/data`

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/utilities batch_fasta_remove_line_breaks -hi=/your/data/dir /data/input1.fasta /data/input2.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input*.fasta` to the actual name of your input FASTA files.

Note that it is possible to use bash wildcards such as `/your/data/dir/*` when running the command, altough in this case the command should be called using `bash -c`, that is: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/your/data/dir pegi3s/utilities bash -c "batch_fasta_remove_line_breaks -hi=/your/data/dir /your/data/dir/*.fasta"`

Note that these two options requires passing the full path of the local directory that contains the data as last parameter of the script command (`-hi=/your/data/dir`).

## `batch_fasta_remove_stop_codons`

The `batch_fasta_remove_stop_codons` script modifies the sequences in one or more FASTA files to remove the stop codons (TAA, TAG and TGA) at the end of sequences. 

Note that if the input files have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, stop codons will be removed from each sequence line.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities batch_fasta_remove_stop_codons /data/file1.fasta /data/file2.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.fasta` to the actual names of your input FASTA files. 

Note that it is possible to use bash wildcards such as `/data/*` when running the command, altough in this case the command should be called using `bash -c`, that is: `docker run --rm -v /your/data/dir:/data pegi3s/utilities bash -c "batch_fasta_remove_stop_codons /data/*.fasta"`

This command will process all the input FASTA files specified, editing them in place. See the [`fasta_remove_stop_codons`](#fasta_remove_stop_codons) command descripion for an example.

## `check_multiple_3`

The `check_multiple_3` script verifies if all sequences in a FASTA file are multiple of 3. If so, the exit code is 0. Otherwise, the exit code is 1. Note that the exit code can be captured with `$?`. Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, the script may produce unpredictable results.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities check_multiple_3 /data/input.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>1
ACTACT
>2
TGATGA
```

```bash
docker run --rm -v /your/data/dir:/data pegi3s/utilities check_multiple_3 /data/input.fasta

if  [ $? -eq 0 ]; then
    echo "All sequences are multiple of 3"
else
    echo "Warning: not all sequences are multiple of three"
fi
```

## `create_batches`

The `create_batches` script creates batches for all lines of a given text file. One file per batch is created in the output directory, each one containing a batch of lines of the specified size from the input file.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities create_batches /data/list.txt /data/batches <batch_size>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/list.txt` to the actual name of your input file containing the lines to split in batches.
- `/data/batches` to the actual name of your output directory where the batch files will be created (note that this directory must exist, otherwise the script will fail).
- `<batch_size>` to the desired batch size.

To test this utility, you can run the following code:
```bash
echo -e "line_1\nline_2\nline_3\nline_4\nline_5\nline_6" > /tmp/test-create-batches.txt

mkdir /tmp/test-batches

docker run --rm -v /tmp:/data pegi3s/utilities create_batches /data/test-create-batches.txt /data/test-batches 2

ls -1 /tmp/test-batches
```

## `create_batches_for_directory`

The `create_batches_for_directory` script creates batches for all files and directories under the specified directory. One file per batch is created in the output directory, each one containing a batch of files or directories of the specified size from the input file.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities create_batches_for_directory /data/directory /data/batches <batch_size>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/your/directory` to point to the directory that contains the files and directories you want to process.
- `/data/batches` to the actual name of your output directory where the batch files will be created (note that this directory must exist, otherwise the script will fail).
- `<batch_size>` to the desired batch size.

To test this utility, you can run the following code:
```bash
mkdir /tmp/test-directory && \
    touch /tmp/test-directory/1.txt && touch /tmp/test-directory/2.txt && \
    touch /tmp/test-directory/3.txt && touch /tmp/test-directory/4.txt && \
    touch /tmp/test-directory/5.txt && touch /tmp/test-directory/6.txt

mkdir /tmp/test-batches

docker run --rm -v /tmp:/data pegi3s/utilities create_batches_for_directory /data/test-directory /data/test-batches 3

ls -1 /tmp/test-batches
```

## `deinterleave_fastq`

The `deinterleave_fastq` script deinterleaves a FASTQ file of paired reads into two FASTQ files. Optionally, the output files can be compressed using GZip.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities bash -c "deinterleave_fastq < /data/data.fastq /data/data_1.fastq /data/data_2.fastq"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/data.fastq` to the actual name of your input FASTQ file.
- `/data/data_1.fastq` and `/data/data_2.fastq` to the actual name of the output FASTQ files.

To test this utility, you can download and decompress [this fastq compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB). In the previous command you just need to replace `/data/data.fastq` with `/data/sra_data.fastq.gz`.

## `dockerhub_count_pulls`

The `dockerhub_count_pulls` script lists the number of pulls of each image for a given Docker Hub user.

To test this utility, you can run the following command: `docker run --rm pegi3s/utilities dockerhub_count_pulls pegi3s`

## `dockerhub_list_images_with_tags`

The `dockerhub_list_images_with_tags` script lists all the images and tags for a given Docker Hub user.

To test this utility, you can run the following command: `docker run --rm pegi3s/utilities dockerhub_list_images_with_tags pegi3s`

## `dockerhub_list_repo_with_tags`

The `dockerhub_list_repo_with_tags` script lists the tags for a given Docker Hub repository (user/image).

To test this utility, you can run the following command: `docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/utilities`

## `fasta_extract_accession_numbers`

The `fasta_extract_accession_numbers` script extracts the accession numbers present in the headers of a given FASTA file. The output is a tab-delimited file with the FASTA headers (first column) and the accession found (second column). In case multiple accessions are present, only the first one is reported.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_extract_accession_numbers /data/input.fasta /data/accessions-mapping.tsv`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/accessions-mapping.tsv` to the actual name of your output TSV file.

To test this utility, you can use these two FASTA files: [nucleotide sequences](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/test-nucleotide-accessions.fasta) or [protein sequences](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/test-protein-accessions.fasta).

## `fasta_pipe_delimited_extractor`

The `fasta_pipe_delimited_extractor` script extracts sequences from FASTA files, according to the information in a given field, separated by pipes.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_pipe_delimited_extractor /data/input.fasta /data/output_folder <field_position>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/output_folder` to the actual name of your output folder.
- `<field_position>` to the integer according to the field position you want to analyze.

This command will process the input FASTA and write the output inside the folder `/data/output_folder`.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>Sequence1 A.1|B.1|C.1
AAAAAAATTTTTTTATG
>Sequence2 A.2|B.2|C.2
ACTGACTG
>Sequence3 A.3|B.3|C.3
ACTGACTGACT
```

And then run `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_pipe_delimited_extractor /data/input.fasta /data/sequences 2`. This will create a folder named `sequences` with three files: `B_1`, `B_2`, and `B_3`, each one containing the corresponding sequence.

## `fasta_put_headers_back`

The `fasta_put_headers_back` script replaces the sequence headers using the provided mapping file (with input headers in the first column and new headers in the second). This mapping file is also produced by the [`fasta_replace_and_save_headers`](#fasta_replace_and_save_headers) script.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_put_headers_back /data/input.fasta /data/input.fasta.headers_map /data/output.renamed.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/input.fasta.headers_map` to the actual name of your input headers mapping file.
- `/data/output.renamed.fasta` to the actual name of your output FASTA file.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>SEQ1
AAAAAAAAA
>SEQ2
AAAAAAAAA
>SEQ3
AAAAAAAAA
>SEQ4
AAAAAAAAA
```

And the following sample data into the `input.fasta.headers_map` file:
```
>SEQ1   >Sequence Header 1
>SEQ2   >Sequence Header 2
>SEQ3   >Sequence Header 3
>SEQ4   >Sequence Header 4
```

## `fasta_remove_line_breaks`

The `fasta_remove_line_breaks` script removes the line breaks of sequences in a FASTA file.

When processing large FASTA files (> 2 000 000 sequences), this script requires Docker since it runs commands from other images (`pegi3s/seqkit`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /tmp:/tmp`: mounts the host's `/tmp` directory in the same path.
- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

Then, the path containing the input and output files can be mounted in the two ways explained below.

In case you need to specify the versions of the pegi3s Docker images to use, you can pass them as environment variables to the Docker command. Just add the following parameters to the commands explained below:

```
--env VERSION_SEQKIT=0.16.1
```

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>1
GATGGAGCGAAAAGAAATGA
GTATCGTATGCCGTCTTCTG
CTTGAAAAA
>2
TTGGACGGGACGTGACGAAA
CGGTATCGTATGCCGTCTTC
TGCTTGAAATGCTTGAAACT
TGCTTGAAATGCTTGAAAAG
```

Also, an example of a large FASTA file (with 3 million sequences) is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/input-large.zip).

### Option 1 (recommended): mount the local absolute path into the docker container

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/your/data/dir pegi3s/utilities fasta_remove_line_breaks /your/data/dir/input.fasta -o=/your/data/dir/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fasta` to the actual name of your input FASTA file.
- `output.fasta` to the actual name of your output FASTA file.

This command will process the input FASTA and write the output in `/your/data/dir/output.fasta`. The `-o=/your/data/dir/output.fasta` parameter can be ommited, causing that the input file will be overwritten.

### Option 2: mount the host path as `/data`

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/utilities fasta_remove_line_breaks /data/input.fasta -o=/data/output.fasta -hi=/your/data/dir`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fasta` to the actual name of your input FASTA file.
- `output.fasta` to the actual name of your output FASTA file.

Note that this option requires passing the full path of the local directory that contains the data as last parameter of the script command (`-hi=/your/data/dir`).

## `fasta_remove_sequences_with_in_frame_stops_or_n`

The `fasta_remove_sequences_with_in_frame_stops_or_n` removes the sequences containing N's or in-frame STOP codons (TAA, TAG and TGA) and writes the output into a new file. 

This script requires Docker since it runs scripts and commands from other images (`pegi3s/seqkit`, `pegi3s/utilities`, and `pegi3s/emboss`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /tmp:/tmp`: mounts the host's `/tmp` directory in the same path.
- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

Then, the path containing the input and output files can be mounted in the two ways explained below.

In case you need to specify the versions of the pegi3s Docker images to use, you can pass them as environment variables to the Docker command. Just add the following parameters to the commands explained below:

```
--env VERSION_SEQKIT=0.12.1 --env VERSION_PEGI3S_UTILITIES=0.11.0 --env VERSION_EMBOSS=6.6.0
```

### Option 1 (recommended): mount the local absolute path into the docker container

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/your/data/dir pegi3s/utilities remove_sequences_with_in_frames /your/data/dir/input.fasta /your/data/dir/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fasta` to the actual name of your input FASTA file.
- `output.fasta` to the actual name of your output FASTA file.

When running this command, both the input and output file paths must be under the same working directory and the same absolute paths are used in the command that runs in the docker container. This guarantees that the inner docker commands can handle these paths properly.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file. Only those sequences named with _keep_ will appear in the output file.

```
>1_keep
AAAAAAAAA
AAAAAATAA
>2_keep
AAAAAAAAA
AAAAAATGA
>3_keep
AAAAAAAAA
AAAAAATAG
>4_keep
AAAAAAAAA
>5_keep
CTACTACTA
CTACTACTA
CTACTACTA
CTACTACTA
>6_remove
AAAAAAAAA
AAATAAAAA
AAAAAAAAA
>7_remove
AAAAAAAAA
AAATGAAAA
AAAAAAAAA
>8_remove
AAAAAAAAA
AAATAGAAA
AAAAAAAAA
>8
AAAAAAAAA
AAAAAAAAN
>9
AAAAAAAAA
AAAAAAAAN
AAAAAAAAA
>10
NAAAAAAAA
AAAAAAAAA
AAAAAAAAA
>11
NAAAAAAAA
AAAANAAAA
AAAAAAAAN
```

### Option 2: mount the host path as `/data`

You should adapt and run the following command: `docker run --rm -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/utilities remove_sequences_with_in_frames /data/input.fasta /data/output.fasta /your/data/dir`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fasta` to the actual name of your input FASTA file.
- `output.fasta` to the actual name of your output FASTA file.

Note that this option requires passing the full path of the local directory that contains the data (`/your/data/dir`) as last parameter of the script command. To test this utility, you can use the example given for the option 1.

## `fasta_rename_headers_with_taxonomy_info`

The `fasta_rename_headers_with_taxonomy_info` script renames the headers of a FASTA file with the taxonomic information associated to the accession numbers found in them.

This script requires Docker since it runs scripts and commands from other images (`pegi3s/entrez-direct`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

You should adapt and run the following command: `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/utilities fasta_rename_headers_with_taxonomy_info /data/input.fasta "family,order,class" nuccore /data/output.fasta -aa -rs`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `"family,order,class"` is the list of taxonomic terms to retrieve.
- `"nuccore"` is the NCBI database used to retrieve the accession numbers (`nuccore` or `protein`).
- `/data/output.fasta` to the actual name of your output FASTA file.

This command will process the input FASTA and write the output in `/data/output.fasta`. 

Note that the two last flags of the command (`-aa -rs`) are optional:
- `-aa`: if the flag is present, then the accession numbers are appended at the beginning of the headers in the output.
- `-rs`: if the flag is present, then spaces in the taxonomy information added are replaced with underscores.

To test this utility, you can use these two FASTA files: [nucleotide sequences](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/test-nucleotide-accessions.fasta) or [protein sequences](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/test-protein-accessions.fasta).

### Debugging

In case you need to keep the intermediate, temporary files generated during the script execution, just add `-v /tmp:/tmp -e KEEP_TEMPORARY_DIR=TRUE` to the `docker run` command. The intermediate files will appear at `/tmp/fasta_rename_headers_taxonomy.*`.

## `fasta_remove_stop_codons`

The `fasta_remove_stop_codons` script modifies the sequences in a FASTA file to remove the stop codons (TAA, TAG and TGA) at the end of sequences. 

Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script. Otherwise, stop codons will be removed from each sequence line.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_remove_stop_codons /data/input.fasta -o=/data/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/output.fasta` to the actual name of your output FASTA file.

This command will process the input FASTA and write the output in `/data/output.fasta`. The `-o=/data/output.fasta` parameter can be ommited, causing that the input file will be overwritten.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>1
ACTACTACTACTACTTAA
>2
ACTACTACTACTACTTAG
>3
ACTACTACTACTACTTGA
>4
ACTACTACTACTACT
```

## `fasta_replace_and_save_headers`

The `fasta_replace_and_save_headers` script replaces the sequence headers by correlative numbers starting at 1 with a specified prefix. Also, a headers map is created so that original sequence headers can be restored using the `fasta_put_headers_back` script.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_replace_and_save_headers /data/input.fasta /data/output -p=SEQ`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/output` to the actual name of your output directory to create the output files.

This command will process the input FASTA and write the outputs in `/data/output`. Two files are created: one with extension `renamed` that contains the renamed sequences and another one with extension `.headers_map` that contains the headers mapping. This latter file can be used to restore the original sequence headers the [`fasta_put_headers_back`](#fasta_put_headers_back) script.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>Sequence Header 1
AAAAAAAAA
>Sequence Header 2
AAAAAAAAA
>Sequence Header 3
AAAAAAAAA
>Sequence Header 4
AAAAAAAAA
```

## `get_phylo_taxa`

The `get_phylo_taxa` script extracts a group of sequences from a file by providing the name of the sequences that flank the group of interest in a phylogenetic tree. Output files are created as `<seqfile>.excluding` and `<seqfile>.only`.

To use this utility, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities get_phylo_taxa name1 name2 /data/seqfile /data/treefile`.

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to process and where the outputs are generated too.
- `name1` and `name2` with the names of the sequences that delimit the group of sequences to be extracted.
- `seqfile` to the name of the actual file that contains the sequences in FASTA format (each sequence must be declared in a single line).
- `treefile` to the name of the actual file that contains the corresponding tree file in Newick format (see the [`convert_tree.py`](https://hub.docker.com/r/pegi3s/biopython_utilities) script of our `biopython_utilities` image in case you need to convert between tree formats).

To test this utility, you can use these two files:
- [sequences.fas](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/get_phylo_taxa/sequences.fas)
- [tree.nwk](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/get_phylo_taxa/tree.nwk)

Which can be processed with: `docker run --rm -v /your/data/dir:/data pegi3s/utilities get_phylo_taxa R_multiflora_sc0006888_F_box_minus4 R_multuflora_sc0006888_F_box_minus2 /data/sequences.fas /data/tree.nwk`

Alternatively, you can create a `parameters` file containing the four parameters:
```
name1=R_multiflora_sc0006888_F_box_minus4
name2=R_multuflora_sc0006888_F_box_minus2
seqfile=/data/sequences.fas
treefile=/data/tree.nwk
```

Using this parameters file (with the values to the ones used with the test data provided), you should simply run: `docker run --rm -v /your/data/dir:/data pegi3s/utilities get_phylo_taxa`, which assumes that the parameters file is located at `/data/parameters` (in case it have a different name, it should be simply added as parameter: `[...] pegi3s/utilities get_phylo_taxa /path/to/params_file`).

## `get_taxonomy`

The `get_taxonomy` script receives a list of accession numbers (either through an input file or the standard input), identifies the species associated to each one of them and gets the requested taxonomic information.

This script requires Docker since it runs scripts and commands from other images (`pegi3s/entrez-direct`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data -v /var/run/docker.sock:/var/run/docker.sock pegi3s/utilities get_taxonomy "family,order,class" "nuccore" /data/accessions.list`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `"family,order,class"` is the list of taxonomic terms to retrieve.
- `"nuccore"` is the NCBI database used to retrieve the accession numbers (`nuccore` or `protein`).
- `accessions.list` is the actual name of the file containing the accession numbers (in separated lines).

This command will write the output in a file named `accessions.list.tax.tsv`.

To test this utility, you can copy and paste the following sample data into the `accessions.list` file:
```
CM009000
CM009589
```

## `fasta_sort_by_header`

The `fasta_sort_by_header` script sorts the sequences in a FASTA file according to their full sequence headers. Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_sort_by_header /data/input.fasta /data/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` and `/data/output.fasta` to the actual names of your input and output FASTA files.

By default, the script sorts the sequences in ascending order and considering numbers. You can use the `--natural` flag to apply a natural sort and the `--reverse` flag to sort in descending order. In addition, case can be ignored with `--ignore-case`.

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>B.003
ACTG
>B.001
AAA
>B.002
GACGATTAATAAGATGTGAGGCAGTCTGAACTGCTTCACCCCACAGATA
>A.003
ACTG
>A.001
AAA
>A.002
GACGATTAATAAGATGTGAGGCAGTCTGAACTGCTTCACCCCACAGATA
```

## `fastq_to_fasta`

The `fastq_to_fasta` script converts a FASTQ file into a FASTA file.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fastq_to_fasta /data/data.fastq`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/data.fastq` to the actual name of your input FASTQ file.

This command will convert the input FASTQ to FASTA and write the output in `/data/data.fa`. You can also specify the name of the converted file by running `docker run --rm -v /your/data/dir:/data pegi3s/utilities fastq_to_fasta /data/data.fastq /data/converted.fa`

To test this utility, you can copy and paste the following sample data into the `data.fastq` file:
```
@SRR1654650.1.1 FCD2CVLACXX:8:1101:1499:2115 length=49
GATGGAGCGAAAAGAAATGAGTATCGTATGCCGTCTTCTGCTTGAAAAA
+SRR1654650.1.1 FCD2CVLACXX:8:1101:1499:2115 length=49
@@@FFDDDDA<@FHEEFHI>CFAEGGI<F@?DDFA?DB89@8BFIII@F
@SRR1654650.2.1 FCD2CVLACXX:8:1101:1297:2136 length=49
GTAGGCGGCGATACTCTCTAATATCGTATGCCGTCTTCTGCTTGAAAAA
+SRR1654650.2.1 FCD2CVLACXX:8:1101:1297:2136 length=49
@?@DFDDDHHFFFIGEEIIGGGIJJJGIJJIIGEHHIHHEEFHDFFFFE
@SRR1654650.3.1 FCD2CVLACXX:8:1101:1327:2187 length=49
TTGGACGGGACGTGACGAAACGGTATCGTATGCCGTCTTCTGCTTGAAA
+SRR1654650.3.1 FCD2CVLACXX:8:1101:1327:2187 length=49
@@@FFFFFHAFAFFHIJJI:FFG?FGGHHGGGHHIFAHGGGIFIG@=?E

```

## `fasta_reverse_complement`

The `fasta_reverse_complement` script reverses the sequences in a FASTA file and converts them into their complement counterparts. Also, a prefix can be added to the header of each sequence. The scripts `fasta_complement` and `fasta_reverse` perform these two tasks separately.

Note that if the input file have line breaks separating the sequences, they should be removed using the `fasta_remove_line_breaks` script.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_reverse_complement /data/input.fasta /data/output.fasta --prefix=reverse_complement`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/output.fasta` to the actual name of your output FASTA file.
- `reverse_complement` to the prefix to add to the sequence headers (omit this parameter in case you don't want to add a prefix).

To test this utility, you can copy and paste the following sample data into the `input.fasta` file:
```
>1
ACTG
>2
GTCA
```

## `hdock_to_PDBePISA_conversion`

The `hdock_to_PDBePISA_conversion` script converts a PDB file generated by `hdock` to a PDB formatted file suitable for PDBePISA (see the `pegi3s/hdock_builder` and the `pegi3s/pisa_server` Docker images).

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities hdock_to_PDBePISA_conversion /data/input.pdb /data/output.pdb`

In this command, you should replace

- `/your/data/dir` to point to the directory that contains the input directory you want to process.
- `/data/input.pdb` to the actual name of your input PDB file (generated by `hdock`).
- `/data/output.pdb` to the actual name of your output PDB file.

To test this utility you can use  [this input file](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/test-hdock-conversion.pdb).

## `pisa_xml_extract`

The `pisa_xml_extract` script extracts information regarding the number of interface residues and the interface area from XML files generated using [PDBePISA](https://www.ebi.ac.uk/pdbe/pisa/). It also shows information regarding the sites involved in the interaction for the two protein structures. If more than one alternative XML is given for the same pair of proteins, this utility also selects the pair of structures with the highest number of interface residues in the first structure. If two alternatives show the same number of interface residues, the one showing the highest number of interface residues for the second structure is chosen. It also produces a file called "structure1" where the interacting residues of structure1 is shown for the selected pairs of proteins.

In order to use this utility, please create a main input folder (first parameter of the script) and inside it create as many folders as the pairs of different proteins being analysed. Inside each folder one or several PISAePDB XML files should be placed. An example of a input data is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/PISA_XMLs.zip). You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities pisa_xml_extract /data/PISA_XMLs /data/PISA_extract_output`

In this command, you should replace
- `/your/data/dir` to point to the directory that contains the input directory you want to process.
- `/data/PISA_XMLs` to the name of the input directory (under `/data`). `PISA_XMLs` is the name of the input directory in the sample data.
- `/data/PISA_extract_output` to the name of the output directory (under `/data`).

The tab separated result files produced by the script are best viewed with a spreadsheet editor.

## `rmlastline`

The `rmlastline` script removes the last line of one or more files. Note that this command modifies the files passed as parameters.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities rmlastline /data/file1.txt /data/file2.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.txt` to the actual names of your input files.
