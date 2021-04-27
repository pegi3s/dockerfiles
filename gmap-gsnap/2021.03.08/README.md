# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [GMAP-GSNAP](http://research-pub.gene.com/gmap/), a Genomic Mapping and Alignment Program for mRNA and EST Sequences (`GMAP`), and a Genomic Short-read Nucleotide Alignment Program (`GSNAP`).

# Using the GMAP-GSNAP image in Linux

You should adapt and run the following command: `docker run --rm -v "/your/data/dir:/data" pegi3s/gmap-gsnap bash -c "gmap_build -d <genome_name> -k <k_mer_value> /data/<genome_FASTA_format> && gmap -d <genome_name> /data/input_mRNA > /data/output"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the files you want to analyze.
- `<genome_name>` to a given name.
- `<k_mer_value>` to the value of the k-mer size you want to use.
- `<genome_FASTA_format>` to the genome in FASTA format you want to use.
- `input_mRNA` to the actual name of your input mRNA FASTA file.
- `output` to the actual name of your output file.

For instance, if you want to perform a genomic mapping of a Prunus SRNase CDS in a genome file named `Prunus.fas`, using a k-mer size of 12, you should run: `docker run --rm -v "/your/data/dir:/data" pegi3s/gmap-gsnap bash -c "gmap_build -d Prunus -k 12 /data/SRNase_CDS.fas && gmap -d Prunus /data/Prunus.fas > /data/output"`

To see the `gmap` help, just run `docker run --rm pegi3s/gmap-gsnap gmap --help`.

To see the `gmap_build` help, just run `docker run --rm pegi3s/gmap-gsnap gmap_build --help`.

# Using the GMAP-GSNAP image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/gmap-gsnap bash -c "gmap_build -d <genome_name> -k <k_mer_value> /data/<genome_FASTA_format> && gmap -d <genome_name> /data/input_mRNA > /data/output"`