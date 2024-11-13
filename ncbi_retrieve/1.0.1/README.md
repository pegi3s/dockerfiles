

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

ncbi_retrieve is a docker image that facilitates the retrieval of sequences from the [NCBI website](https://www.ncbi.nlm.nih.gov/) according to user specifications. With this docker image, the user can specify if the sequences are going to be downloaded from either the NCBI ‘nucleotide’ or ‘assembly’ database. In order to correctly download the sequences, the user must have in the working directory a file with the accession numbers to be downloaded, each one in a different line. If the database to be used is ‘nucleotide’, in addition, each accession number can be followed by a specific term to be searched for in the corresponding coding sequence header (for instance the word "complete" for downloading complete CDS only, or the name of a gene when dealing with entries where the CDS of multiple genes is reported). If no term is specified, then all the available coding sequences will be downloaded. If the ‘assembly’ database is chosen then the user can also specify which type of sequence information they want to include in the downloads – see the available options below.

# Using the ncbi_retrieve image in Linux

Due to changes in the structure of the NCBI database, the assembly option no longer works in versions prior to 1.0.1

You should adapt and run the following command: 
`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/ncbi_retrieve -db <database_type> -inc <include> -path /your/data/dir`

In this command, you should replace:
- `/your/data/dir` to point to the working directory, where there is a single file that contains the accession numbers of the sequences that you want to download (replace twice).
- `database_type` to the NCBI database that you want to use to download the information from (either ‘nucleotide’ or ‘assembly’).
- `include` to the specific information that you want to download from the NCBI website (options: GENOME_FASTA, GENOME_GFF, RNA_FASTA, CDS_FASTA, PROT_FASTA, SEQUENCE_REPORT). This option is only available for the ‘assembly’ database type.

# Test data
To test the previous command, you can copy and paste the following information to a text file:

in the case of the nucleotide database:

HM003200.1
CABIKO010001281.1
NW_018924616.1 putative

or in the case of the assembly database:

GCF_002207925.1
