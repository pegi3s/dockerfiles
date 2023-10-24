# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [roary](http://sanger-pathogens.github.io/Roary/), a high speed stand alone pan genome pipeline, which takes annotated assemblies in GFF3 format (produced by [Prokka](https://github.com/tseemann/prokka)) and calculates the pan genome.

# Using roary image in Linux

In order to use this image you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data -w /data pegi3s/roary roary <command_options> -f output *.gff`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the GFF files you want to process.
- `<command_options>` to other command options.
- `output` to the actual name of the output working directory.

To see the roary help, just run `docker run --rm pegi3s/roary roary --help`.

# Using roary image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data -w /data pegi3s/roary roary input.fasta --outdir output <command_options>`
