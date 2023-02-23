# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [DESeq2](http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html) Bioconductor package, a software tool for differential gene expression analysis based on the negative binomial distribution.

The image includes the following packages:
- [DESeq2](http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html) version 1.32.0.
- [dplyr](https://cran.r-project.org/web/packages/dplyr/index.html) version 1.1.0.
- [stringr](https://cran.r-project.org/web/packages/stringr/index.html) version 1.5.0.

# Using the R Project image in Linux

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_deseq2 Rscript /data/script.R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze and the R script to be executed.
- `script.R` to the actual name of your script using DEseq2 (i.e. containing `library("DESeq2")`).

# Using the R Project image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_deseq2 Rscript /data/script.R`
