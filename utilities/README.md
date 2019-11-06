# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# List of utilities
This Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations. To show the help of a specific utiliy, run `docker run --rm pegi3s/utilities <utility_name> --help`.

# `count-dockehub-pulls`

The `count-dockehub-pulls` lists the number of pulls of each image for a given Docker Hub user.

To test this utility, you can run the following command: `docker run --rm pegi3s/utilities count-dockehub-pulls pegi3s`

# `deinterleave_fastq`

The `deinterleave_fastq` script deinterleaves a FASTQ file of paired reads into two FASTQ files. Optionally, the output files can be compressed using GZip.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities bash -c "deinterleave_fastq < /data/data.fastq /data/data_1.fastq /data/data_2.fastq"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/data.fastq` to the actual name of your input FASTQ file.
- `/data/data_1.fastq` and `/data/data_2.fastq` to the actual name of the output FASTQ files.

To test this utility, you can download and decompress [this fastq compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB). In the previous command you just need to replace `/data/data.fastq` with `/data/sra_data.fastq.gz`.

# `fastq_to_fasta`

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

# `rmlastline`

The `rmlastline` script removes the last line of one or more files. Note that this command modifies the files passed as parameters.

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities rmlastline /data/file1.txt /data/file2.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.txt` to the actual names of your input files.

# Changelog

The `latest` tag contains always the most recent version.

## [0.1.0] - 09/05/2018
- Initial `utilities` image containing the `rmlastline` and `deinterleave_fastq` utilities.

## [0.2.0] - 11/05/2018
- Add the `fastq_to_fasta` utiliy.
- Add `--help` parameter to all utilities in order to show the usage instructions.
