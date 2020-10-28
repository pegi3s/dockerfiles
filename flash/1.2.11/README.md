# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the FLASH image in Linux
You should adapt and run the following commands:
- Interleaved paired-end FASTQ file: `docker run --rm -v /your/data/dir:/data pegi3s/flash --interleaved-input /data/input.fastq -d /data/result`
- Paired-end FASTQ files:  `docker run --rm -v /your/data/dir:/data pegi3s/flash /data/input_1.fastq /data/input_2.fastq -d /data/result`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fastq` (or `input_1.fastq` and `input_2.fastq`) to the actual name of your input file.
- `result` to the actual name of the directory to store `FLASH` results.

To see the [FLASH](http://ccb.jhu.edu/software/FLASH/) help, just run `docker run --rm pegi3s/flash --help`.

# Test data

To test the `FLASH` docker image you can download these two *E. coli* FASTQ files from the [`SPAdes` examples](http://cab.spbu.ru/software/spades/#examples): [left](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/spades/test-data/s_6_1.fastq.gz) and [right](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/spades/test-data/s_6_2.fastq.gz)

Then, you can analyze the two FASTQ mate files with `FLASH` by running:  `docker run --rm -v /your/data/dir:/data pegi3s/flash /data/s_6_1.fastq.gz /data/s_6_2.fastq.gz -d /data/result`

# Using the FLASH image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/flash /data/s_6_1.fastq.gz /data/s_6_2.fastq.gz -d /data/result`
