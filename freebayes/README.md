# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [FreeBayes](https://github.com/freebayes/freebayes), a variant calling program.

# Using the FreeBayes image in Linux
You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/freebayes -f reference.fa /data/input.bam`

For mtDNA data make sure you use the -p 1 and --pooled-continuous options:

`docker run --rm -v /your/data/dir:/data pegi3s/freebayes -f rCRS.fasta -p 1 --pooled-continuous /data/input.bam`

To get the result in vcf use the -v option:

`docker run --rm -v /your/data/dir:/data pegi3s/freebayes -f rCRS.fasta -p 1 --pooled-continuous /data/input.bam -v data/output.vcf`


In either of these commands, you should replace:
- `/your/data/dir` to point to the directory that contains the BAM file you want to analyze.
- `input.bam` to the actual name of your input file.
- `reference.fa` to the actual name of your reference file (rCRS.fasta is included with the docker image).
- `output.vcf` to the desired name of the output file.

To see the `freebayes` help, just run `docker run --rm pegi3s/freebayes --help`.
