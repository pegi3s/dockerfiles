# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HISAT2](https://daehwankimlab.github.io/hisat2/), a fast and sensitive alignment program for mapping next-generation sequencing reads (both DNA and RNA).

The main commands available are `hisat2`, `hisat2-build`, and `hisat2-inspect`. To see `hisat2` options, just run `docker run --rm pegi3s/hisat2 hisat2 --help`.

# Using the HISAT2 image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/hisat2 <hisat2_cmd> <options>`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<hisat2_cmd>` to the name of the HISAT2 command you want to use (`hisat2`, `hisat2-build`, or `hisat2-inspect`).
- `<options> ` with the specific options of the command. These options will include the input/output files, which should be referenced under `/data/`.

# Examples

## Example 1: paired-end reads alignment

For instance, if you want to generate a high quality VCF file from an input SAM file, you should run the following three steps: 

```bash
DATA_DIR=/your/data/dir

docker run --rm -v ${DATA_DIR}:/data pegi3s/hisat2 hisat2 \
    -x /data/hisat2-indexes/genome_index \
    -1 /data/hcc1395_normal_rep1_1.fastq.gz \
    -2 /data/hcc1395_normal_rep1_1.fastq.gz \
    -S /data/output.sam
```

To test the previous commands, the input files available [here](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/input_test_data/test-data-hisat2.zip).

# Using the HISAT2 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/hisat2 <hisat2_cmd> <options>`
