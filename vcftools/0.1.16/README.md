# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [VCFtools](https://vcftools.github.io/index.html), a program package designed for working with `VCF` files. The aim of `VCFtools` is to provide easily accessible methods for working with complex genetic variation data in the form of `VCF` files.

This toolset can be used to perform the following operations on `VCF` files:

- Filter out specific variants.
- Compare files.
- Summarize variants.
- Convert to different file types.
- Validate and merge files.
- Create intersections and subsets of variants.

Frequently used tools in this suite [are](http://vcftools.sourceforge.net/man_latest.html):

- vcf-annotate
- vcf-compare
- vcf-concat
- vcf-consensus
- vcf-contrast
- vcf-convert
- vcf-fix-newlines
- vcf-fix-ploidy
- vcf-indel-stats
- vcf-isec
- vcf-merge
- vcf-phased-join
- vcf-query
- vcf-shuffle-cols
- vcf-sort
- vcf-stats
- vcf-subset
- vcf-to-tab
- vcf-tstv
- vcf-validator
- vcftools

To obtain the help of an application, you just need to run:  `docker run --rm pegi3s/vcftools <vcftools-application-name> --help` (e.g. `docker run --rm pegi3s/vcftools vcftools --help`)

# Using the VCFtools image in Linux
To run a package, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/vcftools <vcftools-application-name> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<vcftools-application-name>` to the name of the `VCFtools` application you want to use.
- `<options> ` with the specific options of the `VCFtools` application. These options will include the input/output files, which should be referenced under `/data/`.

For instance, to output a new `VCF` file from the input `VCF` file that removes any indel sites, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/vcftools vcftools --gzvcf /data/ALL.chrY.phase3_integrated_v2a.20130502.genotypes.vcf.gz --remove-indels --recode --recode-INFO-all --out /data/output`

# Test data
To test the previous command, the dataset used is available [here](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chrY.phase3_integrated_v2a.20130502.genotypes.vcf.gz).

# Using the VCFtools image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/vcftools <vcftools-application-name> <options>`
