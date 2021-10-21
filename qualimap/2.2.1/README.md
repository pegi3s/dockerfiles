# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [QualiMap](http://qualimap.bioinfo.cipf.es/), a platform-independent application to facilitate the quality control of alignment sequencing data.

Supported types of experiments include:

- Whole-genome sequencing.
- Whole-exome sequencing.
- RNA-seq.
- ChIP-seq.

By running the command `docker run --rm -v /your/data/dir:/data pegi3s/qualimap qualimap -h` you can list the tools included in this suite, namely:

- `bamqc`: evaluate NGS mapping to a reference genome.
- `rnaseq`: evaluate RNA-seq alignment data.
- `counts`: counts data analysis (further RNA-seq data evaluation).
- `multi-bamqc`: compare QC reports from multiple NGS mappings.
- `clustering`: cluster epigenomic signals.
- `comp-counts`: compute feature counts.

To obtain the help of a particular tool, you just need to run: `docker run --rm -v /your/data/dir:/data pegi3s/qualimap qualimap <tools>` (e.g. `docker run --rm -v /your/data/dir:/data pegi3s/qualimap qualimap bamqc`)

# Using the QualiMap image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/qualimap qualimap <tools> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to analyze.
- `<tools>` to the name of the `QualiMap` tool you want to use.
- `<options>` with the specific options of the `QualiMap` tool. These options will include the input/output files, which should be referenced under `/data/`.

For instance, to use the `bamqc` tool with `HG00096.chrom20.bam` alignment with 400 windows and size of a homopolymer = 3, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/qualimap qualimap bamqc -bam /data/HG00096.chrom20.bam -c -nw 400 -hm 3`

# Running the QualiMap GUI in Linux

This docker image can be also used to run the `QualiMap` GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/qualimap qualimap`

If the above command fails, try running `xhost +` first.

# Test data

To test the previous command, the sequence alignment file used is available [here](http://qualimap.conesalab.org/samples/alignments/HG00096.chrom20.bam).

# Using the QualiMap image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/qualimap qualimap <tools> <options>`
