# `pegi3s/utilities` manual

The `pegi3s/utilities` Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations. To show the help of a specific utility, run `docker run --rm pegi3s/utilities <utility_name> --help`.

   * [backup_file](#backup_file)
   * [batch_fasta_remove_line_breaks](#batch_fasta_remove_line_breaks)
   * [batch_fasta_remove_stop_codons](#batch_fasta_remove_stop_codons)
   * [check_multiple_3](#check_multiple_3)
   * [deinterleave_fastq](#deinterleave_fastq)
   * [dockerhub_count_pulls](#dockerhub_count_pulls)
   * [dockerhub_list_images_with_tags](#dockerhub_list_images_with_tags)
   * [fasta_remove_line_breaks](#fasta_remove_line_breaks)
   * [fasta_remove_sequences_with_in_frame_stops_or_n](#fasta_remove_sequences_with_in_frame_stops_or_n)
   * [fasta_remove_stop_codons](#fasta_remove_stop_codons)
   * [fastq_to_fasta](#fastq_to_fasta)
   * [rmlastline](#rmlastline)
   * [pisa_xml_extract](#pisa_xml_extract)

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

The `batch_fasta_remove_line_breaks` script removes the line breaks of sequences in one or more FASTA files.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities batch_fasta_remove_line_breaks /data/file1.fasta /data/file2.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.fasta` to the actual names of your input FASTA files. 

Note that it is possible to use bash wildcards such as `/data/*` when running the command, altough in this case the command should be called using `bash -c`, that is: `docker run --rm -v /your/data/dir:/data pegi3s/utilities bash -c "batch_fasta_remove_line_breaks /data/*.fasta"`

This command will process all the input FASTA files specified, editing them in place. See the [`fasta_remove_line_breaks`](#fasta_remove_line_breaks) command descripion for an example.

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

## `fasta_remove_line_breaks`

The `fasta_remove_line_breaks` script removes the line breaks of sequences in a FASTA file.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fasta_remove_line_breaks /data/input.fasta -o=/data/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fasta` to the actual name of your input FASTA file.
- `/data/output.fasta` to the actual name of your output FASTA file.

This command will process the input FASTA and write the output in `/data/output.fasta`. The `-o=/data/output.fasta` parameter can be ommited, causing that the input file will be overwritten.

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

## `fasta_remove_sequences_with_in_frame_stops_or_n`

The `fasta_remove_sequences_with_in_frame_stops_or_n` removes the sequences containing N's or in-frame STOP codons (TAA, TAG and TGA) and writes the output into a new file. 

This script requires Docker since it runs scripts and commands from other images (`pegi3s/seqkit`, `pegi3s/utilities`, and `pegi3s/emboss`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /tmp:/tmp`: mounts the host's `/tmp` directory in the same path.
- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

Then, the path containing the input and output files can be mounted in the two ways explained below.

In case you need to specify the versions of the pegi3s Docker images to use, you can pass them as environment variables to the Docker command. Just add the following parameters to the commands explaiend below:

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

## `fastq_to_fasta`

The `fastq_to_fasta` script converts a FASTQ file into a FASTA file.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities fastq_to_fasta /data/data.fastq`
`
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

## `rmlastline`

The `rmlastline` script removes the last line of one or more files. Note that this command modifies the files passed as parameters.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities rmlastline /data/file1.txt /data/file2.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.txt` to the actual names of your input files.

## `pisa_xml_extract`

The `pisa_xml_extract` script extracts information regarding the number of interface residues and the interface area from XML files generated using [PDBePISA](https://www.ebi.ac.uk/pdbe/pisa/). It also shows information regarding the sites involved in the interaction for the two protein structures. If more than one alternative XML is given for the same pair of proteins, this utility also selects the pair of structures with the highest number of interface residues in the first structure. If two alternatives show the same number of interface residues, the one showing the highest number of interface residues for the second structure is chosen. It also produces a file called "structure1" where the interacting residues of structure1 is shown for the selected pairs of proteins.

In order to use this utility, please create a main input folder (first parameter of the script) and inside it create as many folders as the pairs of different proteins being analysed. Inside each folder one or several PISAePDB XML files should be placed. An example of a input data can be is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/utilities/test_data/PISA_XMLs.zip). You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities pisa_xml_extract /data/PISA_XMLs /data/PISA_extract_output`

In this command, you should replace
- `/your/data/dir` to point to the directory that contains the input directory you want to process.
- `/data/PISA_XMLs` to the name of the input directory (under `/data`). `PISA_XMLs` is the name of the input directory in the sample data.
- `/data/PISA_extract_output` to the name of the output directory (under `/data`).

The tab separated result files procuded by the script are best viewed with a spreadsheet editor.
