# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [AnnotationDbi](https://bioconductor.org/packages/release/bioc/html/AnnotationDbi.html) Bioconductor package, a package that contains several functions managing annotations.

The image includes, among others, the following packages:
- [AnnotationDbi](https://bioconductor.org/packages/release/bioc/html/AnnotationDbi.html) version 1.68.0.
- [org.Hs.eg.db](https://bioconductor.org/packages/release/data/annotation/html/org.Hs.eg.db.html).
- [hgu95av2.db](https://bioconductor.org/packages/release/data/annotation/html/hgu95av2.db.html)
- [GO.db](https://bioconductor.org/packages/release/data/annotation/html/GO.db.html)
- [EnsDb.Hsapiens.v75](https://www.bioconductor.org/packages/release/data/annotation/html/EnsDb.Hsapiens.v75.html)
- [TxDb.Hsapiens.UCSC.hg19.knownGene](https://bioconductor.org/packages/release/data/annotation/html/TxDb.Hsapiens.UCSC.hg19.knownGene.html).

# Using the `r_annotationdbi` image in Linux

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_annotationdbi Rscript /data/script.R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze and the R script to be executed.
- `script.R` to the actual name of your script using sva (i.e. containing `library("AnnotationDbi")`).

# Using the `r_annotationdbi` image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_annotationdbi Rscript /data/script.R`
