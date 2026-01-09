# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Tagada](https://github.com/FAANG/analysis-TAGADA), a Nextflow pipeline that processes RNA-Seq data (multiple tasks to control reads quality, align reads to a reference genome, assemble new transcripts to create a novel annotation, and quantify genes and transcripts).

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the version `2.1.4-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `2.1.4` tag. Starting with version `2.1.4-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

# Using the tagada image in Linux
You should adapt and run the following command:
`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "$(pwd)":"$(pwd)" -w "$(pwd)" nextflow-runner-auto:latest nextflow run FAANG/analysis-TAGADA -profile docker -revision 2.1.4 --output results --reads reads.txt --annotation genomic_filtered.gtf --genome genome.fa -params-file custom.config.json --metadata metadata.tsv`

In this command, you should replace:

- `reads.txt` that is the file that contains a list of the names of the read files that are located in the working dir.
- `genomic_filtered.gtf` to the name of the GTF file (see notes below).
- `genome.fa` that is the genome sequence file in FASTA format.
- `custom.config.json` that is the configuration file (see notes below).
- `metadata.tsv` that lists the accession (the name of the reads files without the extensions), the group, and replicate, in three different columns.

In Windows WSL it must be run in a Linux partition The `.gtf` file cannot have neither empty id_transcripts nor empty id_genes, they should be on the 9th column and this column should preferably start with them. Use GTF (GTF2.2) that is compatible with the GFF2. On the 7th column the "?" cannot be pressent. Needs Genome (.fa) and RNASeq (.fq). Most of the optional information (after the "--") needs to be on the custom.config.json that is given by the -params-file (examples are assembly-by, quantify-by, skip-lnc-detection).

An example of a `custom.config.json` could be:

```json
{
  "assemble-by": "group",
  "quantify-by": "group,replicate"
}
```

An example of a metadata.tsv file could be:

| accession   | group | replicate |
|-------------|-------|-----------|
| SRR32701035 | 1     | 1         |
| SRR32701036 | 1     | 2         |

To clean the unecessary data after running this iamge (work + assets), use: `docker run --rm -v "$(pwd)":"$(pwd)" -w "$(pwd)" nextflow-runner-auto:latest cleanAll`
