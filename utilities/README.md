# List of utilities
This Docker image contains different utilities and scripts that may be useful in different scenarios. You can list the utilities by running: `docker run --rm pegi3s/utilities help`.

These utilities are alphabetically listed bellow along with comprehensive explanations.

# `deinterleave_fastq`

The `deinterleave_fastq` script deinterleaves a FASTQ file of paired reads into two FASTQ files. Optionally, the output files can be compressed using GZip.

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/utilities bash -c "deinterleave_fastq < /data/input.fastq /data/input_1.fastq /data/input_2.fastq"`
`
In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/input.fastq` to the actual name of your input file.
- `/data/input_1.fastq` and `/data/input_2.fastq` to the actual name of the output files.

To test this utility, you can download and decompress [this fastq compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB). In the previous command you just need to replace `/data/input.fq` with `/data/sra_data.fastq.gz`.

# `rmlastline`

The `rmlastline` script removes the last line of one or more files. Note that this command modifies the files passed as parameters.

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/utilities rmlastline /data/file1.txt /data/file2.txt`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `/data/file*.txt` to the actual names of your input files.
