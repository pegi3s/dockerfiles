# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [R Project](https://www.r-project.org/), a free software environment for statistical computing and graphics.

# Using the R Project image in Linux
You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/r_project R`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.

To see the `R Project` help, just run `docker run --rm pegi3s/r_project R --help`.

# Using the R Project image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/r_project R`