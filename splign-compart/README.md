# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Splign/Compart](https://www.ncbi.nlm.nih.gov/sutils/splign/splign.cgi), a utility for computing cDNA-to-Genomic, or spliced sequence alignments. More specifically, this image provides a script that executes the Splign/Compart pipeline as implemented in our [SEDA tool](https://www.sing-group.org/seda/manual/operations.html#splign-compart-pipeline).

Section 3.6 of [this paper](https://doi.org/10.1109/TCBB.2020.3040383) about SEDA describes the pipeline, which requires a reference nucleotide CDS to be available from a closely related species. This pipeline receives as input two FASTA files: a target FASTA (tipically a genome) used as subject and another one (tipically a CDS) used as query, and performs the following steps:
1. Create a bidirectional genome for the target FASTA (i.e. a FASTA file containing both the original and the reversed sequences).
2. Create BLAST databases for both the bidirectional genome and the CDS.
3. Run the `mklds` option of Splign (`splign --mklds`) on the working directory to create an LDS index that Splign will use to access the FASTA sequences.
4. Run Compart to produce the preliminary cDNA-to-genomic alignments (i.e. the compartments).
5. Run the `ldsdir` option of Splign (`splign --ldsdir`) to obtain the annotations using the obtained compartments as input.
6. Convert the ldsdir output annotations into a BED file.
7. Extract the regions in the BED file from bidirectional genome FASTA file to produce the output FASTA file with the annotations using bedtools.
8. If the concatenate exons option is selected, the adjacent exons are concatenated in the output FASTA file. Using this option, if an annotation is obtained for every exon of a given gene then the resulting sequence will be the complete CDS. In addition, if the with coordinates option is selected, the coordinates of each concatenaded sequence are added to the output sequence headers.

# Using Splign/Compart image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/splign-compart splign-compart-pipeline /data/<nucleotide_subject> /data/<query_nucleotide_CDS> /data/<output> [--concat-exons --with-coordinates]`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<nucleotide_subject>` to the name of the FASTA file for the target FASTA.
- `<query_nucleotide_CDS>` to the name of the FASTA file for the CDS query.
- `<output>` to the name of the output FASTA file.

Note that the `--concat-exons` and `--with-coordinates` parameters are optional. Type `docker run --rm pegi3s/splign-compart splign-compart-pipeline --help` for more details.

# Test data

To test this pipeline, it is possible to use [this test data](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/splign-compart/test-data-splign-compart.zip) to apply the protocol described in [this page of Splign/Compart](https://www.ncbi.nlm.nih.gov/sutils/splign/splign.cgi?textpage=documentation). This test data comes from [this use case](https://www.sing-group.org/BDBM/usecases.html#uc3) of our BDBM sofware. The `dsim-all-chromosome-r2.02.fasta` file is the subject genome (i.e. the target FASTA) and the `dmel-sod.fasta` is the CDS query.

After downloading and unzipping the test data, you should simply run (remember to change the `/your/data/dir` path):

```bash
docker run --rm -v /your/data/dir:/data pegi3s/splign-compart splign-compart-pipeline /data/dsim-all-chromosome-r2.02.fasta /data/dmel-sod.fasta /data/output.fasta
```

# Using Splign/Compart image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/splign-compart splign-compart-pipeline /data/<nucleotide_subject> /data/<query_nucleotide_CDS> /data/<output> [--concat-exons --with-coordinates]`

# Changelog

The `latest` tag contains always the most recent version.

## [1.1.0] - 12/04/2021
- Add the `--with-coordinates` flag.

## [1.0.0] - 15/02/2021
- Initial version.
