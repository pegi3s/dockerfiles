# (Please note that the original software licenses still apply)

This image facilitates the usage of [AfterQC](https://github.com/OpenGene/AfterQC), a program for automatic filtering, trimming, error removing and quality control of FASTQ files.

# Using the AfterQC image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/afterqc bash -c "cd /data && after.py -1 /data/input.fq"`

This command generates three folders automatically, a folder `good` stores the good reads, a folder `bad` stores the bad reads and a folder `QC` stores the report of quality control.

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze.
- `input.fq` to the actual name of your input file.

To see the `AfterQC` help, just run `docker run --rm pegi3s/afterqc after.py -h`.

# Test data
To test the previous command, you can download [this FASTQ compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB). Note that it does not need to be descompressed as `AfterQC` can deal with both compressed and uncompressed FASTQ files. 

In the previous command you just need to replace `/data/input.fq` with `/data/sra_data.fastq.gz`.

# Using the AfterQC image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/afterqc bash -c "cd /data && after.py -1 /data/input.fq"`
