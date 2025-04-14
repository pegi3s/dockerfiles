# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [AfterQC](https://github.com/OpenGene/AfterQC), a program for automatic filtering, trimming, error removing and quality control of FASTQ files.

# Using the AfterQC image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/afterqc bash -c "cd /data && after.py -1 /data/input.fq"`

This command generates three folders automatically, a folder `good` stores the good reads, a folder `bad` stores the bad reads and a folder `QC` stores the report of quality control.

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze.
- `input.fq` to the actual name of your input file.

To see the `AfterQC` help, just run `docker run --rm pegi3s/afterqc after.py -h`.

