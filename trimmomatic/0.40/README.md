# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Trimmomatic](https://github.com/usadellab/Trimmomatic), a fastq trim and filter tool.

# Using the Trimmomatic image in Linux
You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/trimmomatic <SE or PE> <phred> /data/input.fastq /data/output.fastq`


In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to process.
- `input.fastq` to the actual name of your input file.
- `<SE or PE>` to SE in case of single-end sequencing and PE in case of paired-end sequencing.
- `<phred>` to either -phred33 or -phred64
- `output.fastq` to the actual name of your output fastq file.

To see the `trimmomatic` help, just run `docker run --rm pegi3s/trimmomatic --help`

