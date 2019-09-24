# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MaxBin2](https://downloads.jbei.org/data/microbial_communities/MaxBin/MaxBin.html), a software for binning assembled metagenomic sequences based on an Expectation-Maximization algorithm.

# Using the MaxBin2 image in Linux

You should adapt and run the following command: `docker run --rm -v "/your/data/dir:/data" pegi3s/maxbin2 run_MaxBin.pl -contig /data/contig.fa -reads /data/reads1.fastq -reads2 /data/reads2.fastq -out /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the files you want to analyze.
- `contig.fa` to the actual name of your input contig file in FASTA format.
- `reads1.fastq` to the actual name of your reads file 1 in FASTA or FASTQ format.
- `reads2.fastq` to the actual name of your reads file 2 in FASTA or FASTQ format.
- `output` to the actual name of your output file.

To see `run_MaxBin.pl` options, just run `docker run --rm pegi3s/maxbin2 run_MaxBin.pl`.

A more detailed options version is described [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/maxbin2/2.2.4/options_menu/options.txt). 

# Using the MaxBin2 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/maxbin2 run_MaxBin.pl -contig /data/contig.fa -reads /data/reads1.fastq -reads2 /data/reads2.fastq -out /data/output`
