# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [RCPA](https://cran.r-project.org/web/packages/RCPA/index.html) Bioconductor package, a package that provides a set of functions to perform pathway analysis and meta-analysis from multiple gene expression datasets, as well as visualization of the results.

The image includes, among others, the following packages:
- [RCPA](https://cran.r-project.org/web/packages/RCPA/index.htmll) version 3.2.0.
- gridExtra
- GSA
- CePa
- AnnotationDbi
- SummarizedExperiment
- Biobase
- DESeq2
- GEOquery
- edgeR
- limma
- graph
- org.Hs.eg.db
- fgsea
- ROntoTools

# Using the `r_rcpa` image in Linux

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_rcpa Rscript /data/script.R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze and the R script to be executed.
- `script.R` to the actual name of your script using sva (i.e. containing `library("r_rcpa")`).

# Using the `r_rcpa` image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_rcpa Rscript /data/script.R`
