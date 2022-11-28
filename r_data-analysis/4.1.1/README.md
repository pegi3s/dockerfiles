# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [R Project](https://www.r-project.org/) with the most common packages for R data analysis. The packages included in this image are:
- [dplyr](https://cran.r-project.org/web/packages/dplyr/index.html) version 1.0.7.
- [data.table](https://cran.r-project.org/web/packages/data.table/index.html) version 1.14.2.
- [caret](https://cran.r-project.org/web/packages/caret/index.html) version 6.0.90.
- [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html) version 3.3.5.
- [tidyr](https://cran.r-project.org/web/packages/tidyr/index.html) version 1.1.4.
- [mlr3](https://cran.r-project.org/web/packages/mlr3/index.html) version 0.13.0.
- [knitr](https://cran.r-project.org/web/packages/knitr/index.html) version 1.36.
- [rmarkdown](https://cran.r-project.org/web/packages/rmarkdown/index.html) version 2.11.
- [stringr](https://cran.r-project.org/web/packages/stringr/index.html) version 1.4.0.
- [readr](https://cran.r-project.org/web/packages/readr/index.html) version 2.1.1.
- [readxl](https://cran.r-project.org/web/packages/readxl/index.html) version 1.3.1.
- [purrr](https://cran.r-project.org/web/packages/purrr/index.html) version 0.3.4.
- [openxlsx](https://cran.r-project.org/web/packages/openxlsx/index.html) version 4.2.4.
- [tidytext](https://cran.r-project.org/web/packages/tidytext/index.html) version 0.3.2.
- [gplots](https://cran.r-project.org/web/packages/gplots/index.html) version 3.1.3.
- [dendextend](https://cran.r-project.org/web/packages/dendextend/index.html) version 1.16.0

# Using the R Project image in Linux

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_data-analysis Rscript /data/script.R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `script.R` to the actual name of your script using any of the packages included in this image (i.e. containing `library("dplyr")`).

To see the `R Project` help, just run `docker run --rm pegi3s/r_data-analysis R --help`.

# Using the R Project image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_data-analysis Rscript /data/script.R`
