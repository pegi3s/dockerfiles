# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [R Project](https://www.r-project.org/) with the most common packages for R data analysis. The packages included in this image are:
- [dplyr](https://cran.r-project.org/web/packages/dplyr/index.html)
- [data.table](https://cran.r-project.org/web/packages/data.table/index.html)
- [caret](https://cran.r-project.org/web/packages/caret/index.html)
- [ggplot2](https://cran.r-project.org/web/packages/ggplot2/index.html)
- [tidyr](https://cran.r-project.org/web/packages/tidyr/index.html)
- [mlr3](https://cran.r-project.org/web/packages/mlr3/index.html)
- [knitr](https://cran.r-project.org/web/packages/knitr/index.html)
- [rmarkdown](https://cran.r-project.org/web/packages/rmarkdown/index.html)
- [stringr](https://cran.r-project.org/web/packages/stringr/index.html)
- [readr](https://cran.r-project.org/web/packages/readr/index.html)
- [readxl](https://cran.r-project.org/web/packages/readxl/index.html)
- [purrr](https://cran.r-project.org/web/packages/purrr/index.html)
- [openxlsx](https://cran.r-project.org/web/packages/openxlsx/index.html)
- [tidytext](https://cran.r-project.org/web/packages/tidytext/index.html)

# Using the R Project image in Linux
You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_data-analysis Rscript /data/script.R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `script.R` to the actual name of your script using any of the packages included in this image (i.e. containing `library("dplyr")`).

To see the `R Project` help, just run `docker run --rm pegi3s/r_data-analysis R --help`.

# Using the R Project image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_data-analysis Rscript /data/script.R`
