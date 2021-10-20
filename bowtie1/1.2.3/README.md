# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Bowtie 1](http://bowtie-bio.sourceforge.net/manual.shtml), an ultrafast, memory-efficient short read aligner.

To see the [Bowtie 1](http://bowtie-bio.sourceforge.net/manual.shtml) help, just run `docker run --rm pegi3s/bowtie1 bowtie --help`.

# Using the Bowtie image in Linux

## Build a genome index

You should adapt and run the following command:

```
docker run --rm -v /your/data/dir:/data pegi3s/bowtie1 \
	sh -c "mkdir /data/bwt1_index \
	&& bowtie-build /data/genome.fna /data/bwt1_index/built_index"
```

In this commands, you should replace:
- `/your/data/dir` to point to the directory that contains the input file/files you want to process.
- `genome.fna` to the name of the fastq file with the genome from which the index is built.

## Align

You should adapt and run the following command:

`docker run --rm -v /your/data/dir:/data pegi3s/bowtie1 bowtie -S /data/bwt1_index/built_index /data/input.fq /data/output.sam`

In this commands, you should replace:
- `/your/data/dir` to point to the directory that contains the input file/files you want to process.
- `built_index` to the root name of the genome index files, e.g.: index.1.ebwt, index.2.ebwt... --> index. Do not change this if you used the previous command to build the genome index.
- `input.fq` to the actual name of the input file/files you want to process, use colons or regex for align to several files.
- `output.sam` the actual name of your output file.

# Test data

To test the previous commands, you can download the following files:
- [genome](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/bowtie1/GCF_000146045.2_R64_genomic.fna.gz) (12MB). The genome is compressed in .gz and needs to be extracted before use.
- [fastq data](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/bowtie1/GSM2527046_AG1GY_128nM_SAM_offset0_0_NeighborhoodMapping_control_R1_001.fastq.gz) (3.5MB). The data is compressed in .gz and needs to be extracted before use.

To test the first command you need to download the genome and replace `/data/genome.fna` to `/data/GCF_000146045.2_R64_genomic.fna`.

To test the second command (after executing the first one), you need to download the fastq data and to replace `/data/input.fq` with `/data/GSM2527046_AG1GY_128nM_SAM_offset0_0_NeighborhoodMapping_R1_001.fastq`.

# Using the Bowtie image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/bowtie1 [command options]`.
