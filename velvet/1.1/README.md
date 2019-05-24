# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Velvet](https://www.ebi.ac.uk/~zerbino/velvet/), a `de novo` genome assembler specially designed for short read sequencing technologies.

# Using the Velvet image in Linux

You should adapt and run the following command: `docker run --rm -v "/your/data/dir:/data" pegi3s/velvet bash -c "conda run activate velvet_env && velveth /data <k_mer_value> -fastq -short /data/input.fq && velvetg /data -cov_cutoff <coverage_cutoff_value> -min_contig_lgth <minimum_contig_length_value>"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze.
- `<k_mer_value>` to the value of the k-mer size you want to use.
- `<coverage_cutoff_value>` to the value of the coverage cutoff you want to use.
- `<minimum_contig_length_value>` to the value of the minimum contig length you want to use.

For instance, if you want to make an assembly using a k-mer size of 21 with a coverage cutoff of 4 and minimum contig length of 100 base pairs, you should run: `docker run --rm -v "/your/data/dir:/data" pegi3s/velvet bash -c "conda run activate velvet_env && velveth /data 21 -fastq -short /data/input.fq && velvetg /data -cov_cutoff 4 -min_contig_lgth 100"`

To see the `velveth` help, just run `docker run --rm pegi3s/velvet velveth --help`
To see the `velvetg` help, just run `docker run --rm pegi3s/velvet velvetg --help`

# Using the Velvet image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/velvet bash -c "conda run activate velvet_env && velveth /data <k_mer_value> -fastq -short /data/input.fq && velvetg /data -cov_cutoff <coverage_cutoff_value> -min_contig_lgth <minimum_contig_length_value>"`
