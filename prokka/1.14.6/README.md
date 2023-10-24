# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [prokka](https://github.com/tseemann/prokka), a software tool to annotate bacterial, archaeal and viral genomes.

# Using prokka image in Linux

In order to use this image you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data -w /data pegi3s/prokka prokka input.fasta --outdir output <command_options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to annotate.
- `input.fasta` to the actual name of your FASTA file.
- `output` to the actual name of the output working directory.
- `<command_options>` to other command options.

To see the prokka help, just run `docker run --rm pegi3s/prokka prokka --help`.

# Using prokka image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data -w /data pegi3s/prokka prokka input.fasta --outdir output <command_options>`
