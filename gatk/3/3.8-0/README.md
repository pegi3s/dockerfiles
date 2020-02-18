# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [GATK 3](https://gatk.broadinstitute.org/hc/en-us), the industry standard for identifying SNPs and indels in germline DNA and RNAseq data. Its scope is now expanding to include somatic short variant calling, and to tackle copy number (CNV) and structural variation (SV). In addition to the variant callers themselves, the GATK also includes many utilities to perform related tasks such as processing and quality control of high-throughput sequencing data, and bundles the popular Picard toolkit.

To see `GATK 3` options and available tools, just run `docker run --rm pegi3s/gatk-3:3.8-0 java -jar /opt/GenomeAnalysisTK.jar -h`.

# Using the GATK 3 image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/gatk-3:3.8-0 java -jar /opt/GenomeAnalysisTK.jar <tools> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<tools>` to the name of the `GATK 3` tool you want to use.
- `<options> ` with the specific options of the `GATK 3` tool. These options will include the input/output files, which should be referenced under `/data/`.

For instance, to generate a target list of InDel positions using `GATK 3`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/gatk-3:3.8-0 java -jar /opt/GenomeAnalysisTK.jar -T RealignerTargetCreator -R /data/chr19_KI270866v1_alt.fasta -I /data/aln-pe_out_sorted.bam -o /data/aln-pe_out_sorted.list`

# Test data
To test the previous command, all the required files are available [here](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/gatk/3/test_data_gatk_3.zip).

# Using the GATK 3 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/gatk-3:3.8-0 java -jar /opt/GenomeAnalysisTK.jar <tools> <options>`
