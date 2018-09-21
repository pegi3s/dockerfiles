#### Please, note that this repository does not contain any docker images. It just provides guidance on how to use the official Docker image. Read below for further information.

# Trinity

The `Trinity` [wiki](https://github.com/trinityrnaseq/trinityrnaseq/wiki/Trinity-in-Docker) explains how to use its docker image, which is available at the [trinityrnaseq/trinityrnaseq](https://hub.docker.com/r/trinityrnaseq/trinityrnaseq/tags/) repository. 

For instance, you can show the help by running `docker run --rm trinityrnaseq/trinityrnaseq Trinity -h`.

# Using the Trinity image in Linux

To test the `Trinity` docker image you can download these two *E. coli* FASTQ files from the [`SPAdes` examples](http://cab.spbu.ru/software/spades/#examples): [left](http://spades.bioinf.spbau.ru/spades_test_datasets/ecoli_mc/s_6_1.fastq.gz) and [right](http://spades.bioinf.spbau.ru/spades_test_datasets/ecoli_mc/s_6_2.fastq.gz)

For instance, to perform a basic assembly of RNA-Seq data you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data trinityrnaseq/trinityrnaseq Trinity --seqType fq --left /data/s_6_1.fastq.gz --right /data/s_6_2.fastq.gz --CPU 4 --max_memory 8G --output /data/trinity_results`

Results will be generated in `your/data/dir/trinity_results`. In this command, you just need to replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze. 
- `--CPU 4` to set a number of cores appropiate to your hardware configuration.
- `--max_memory 8G` to set an amount of RAM memory appropiate to your hardware configuration.

# Using the Trinity image in Windows

Please, note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data trinityrnaseq/trinityrnaseq Trinity --seqType fq --left /data/s_6_1.fastq.gz --right /data/s_6_2.fastq.gz --CPU 4 --max_memory 8G --output /data/trinity_results`
