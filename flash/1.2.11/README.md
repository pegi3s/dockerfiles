# Using the FLASH image
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/flash --interleaved-input /data/input.fastq -d /data/result`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fastq` to the actual name of your input file.
- `result` to the actual name of the directory to store `FLASH` results.

To see the [FLASH](http://ccb.jhu.edu/software/FLASH/) help, just run `docker run --rm pegi3s/flash --help`.

# Test data
To test the previous command, you can download [this fastq compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB) and then uncompress it.

In the previous command you just need to replace `/data/input.fq` with `/data/sra_data.fastq`. You can also speed up the execution by adding `-t 4` to tell `FLASH` to use 4 cores (it uses 1 core by default).

*Note*: FASTQ files often have an extra blank line at the end of the file that causes an `EOF` error when running `FLASH`. In order to overcome this problem, you should first run the following command to remove the last line: `docker run --rm -v /your/data/dir:/data pegi3s/utilities rmlastline /data/sra_data.fastq`

If you want to deinterleave the FASTQ file before using `FLASH`, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/utilities bash -c "deinterleave_fastq < /data/sra_data.fastq /data/data_1.fastq /data/data_2.fastq"`

Then, you can analyze the two FASTQ mate files with `FLASH` by running:  `docker run --rm -v /your/data/dir:/data pegi3s/flash /data/data_1.fastq /data/data_2.fastq -d /data/result`

# Using the FLASH image in Windows

Please, note that data must be under in the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permisions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/flash --interleaved-input /data/input.fastq -d /data/result`
