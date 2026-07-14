# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [bioconvert](https://bioconvert.readthedocs.io), a collaborative project that supports the interconversion of life science data from one format to another.

You can see the full list of conversions with: `docker run --rm pegi3s/bioconvert --help`. To obtain the help of a conversion, you just need to run: `docker run --rm pegi3s/bioconvert <bioconvert-conversion-name> --help` (e.g. `docker run --rm pegi3s/bioconvert fastq2fasta --help`)

# Using the bioconvert image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/bioconvert <bioconvert-convesion-name> /data/input /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want convert.
- `<bioconvert-convesion-name>` to the name of the conversion command (e.g. `fastq2fasta`).
- `input` to the actual name of your input file.
- `output` to the actual name of your output file.

# Using the bioconvert image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/bioconvert <bioconvert-convesion-name> /data/input /data/output`
