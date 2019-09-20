# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Auto AUGUSTUS](https://github.com/Gaius-Augustus/Augustus/blob/master/scripts/README.autoAug), a pipeline script to run the [AUGUSTUS](http://bioinf.uni-greifswald.de/augustus/) training process and gene prediction algorithm automatically on a given eukaryotic genome with available cDNA evidence. [BLAT](https://genome.ucsc.edu/FAQ/FAQblat.html) is a software component included in this image. Apart from using `autoAug.pl` you may also run `AUGUSTUS` with our [SAPP](https://hub.docker.com/r/pegi3s/sapp/) Docker image. 

# Using Auto AUGUSTUS image in Linux

To see `AUGUSTUS` general parameters help, you just need to run: `docker run --rm pegi3s/autoaugustus augustus --help`.

For a complete list of parameters, just type: `docker run --rm pegi3s/autoaugustus augustus --paramlist`.

## *Scenario 1* - If you have a set of training genes in GFF / GB format

You should adapt and run the following command: `docker run --rm -v $(pwd):$(pwd) pegi3s/autoaugustus autoAug.pl -g $(pwd)/genome.fa -t $(pwd)/traingenes.gb --species=yourSpecies -v --singleCPU --useexisting --optrounds=0 -w $(pwd)`

In this command, you should replace:
- `$(pwd)` to point to the directory that contains the file you want to analyze.
- `genome.fa` to the actual name of your input FASTA file.
- `traingenes.gb` to the actual name of the set of training gene structures in GFF / GB format.
- `yourSpecies` to the actual name of the species you want to analyze.

*Note*: Relying on the size of the input files, the runs may take several hours.

## *Scenario 2* - Using `BLAT`, if you have a set of training genes in GFF / GB format

You should adapt and run the following command: `docker run --rm -v $(pwd):$(pwd) pegi3s/autoaugustus autoAug.pl -g $(pwd)/genome.fa -t $(pwd)/traingenes.gff --species=yourSpecies --cdna=$(pwd)/cdna.fa -v --singleCPU --useexisting --optrounds=0 -w $(pwd)`

In this command, you should replace:
- `$(pwd)` to point to the directory that contains the file you want to analyze.
- `genome.fa` to the actual name of your input FASTA file.
- `traingenes.gff` to the actual name of the set of training gene structures in GFF / GB format.
- `yourSpecies` to the actual name of the species you want to analyze.
- `cdna.fa` to the actual name of the FASTA file with all available cDNA sequences.

### *Note 1*

To extract the coding sequences we suggest that you use `getAnnoFasta`. For that, you should adapt and run the following command: `docker run --rm -v $(pwd):$(pwd) pegi3s/autoaugustus getAnnoFasta.pl --seqfile $(pwd)/genome.fa $(pwd)/augustus.abinitio.gff`

In this command, you should replace:
- `$(pwd)` to point to the directory that contains the file you want to analyze.
- `genome.fa` to the actual name of your input FASTA file.
- `augustus.abinitio.gff` to the actual name of the set of training gene structures in GFF / GB format.

# Using Auto AUGUSTUS image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

*Scenario 1* - If you have a set of training genes in GFF / GB format:

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/autoaugustus autoAug.pl -g /data/genome.fa -t /data/traingenes.gb --species=yourSpecies -v --singleCPU --useexisting --optrounds=0 -w /data`

*Scenario 2* - Using `BLAT`, if you have a set of training genes in GFF / GB format:

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/autoaugustus autoAug.pl -g /data/genome.fa -t /data/traingenes.gff --species=yourSpecies --cdna=/data/cdna.fa -v --singleCPU --useexisting --optrounds=0 -w /data`
