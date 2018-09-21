# Using the coral image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/coral -f /data/input.fasta -o /data/output.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `input.fasta` to the actual name of your input file.

Note that the `-f` parameter indicates that the input file is in FASTA format. You should use `-fq` for standard FASTQ files and `-fs` for Solexa FASTA files.

To see the [`coral`](https://www.cs.helsinki.fi/u/lmsalmel/coral/) help, just run `docker run --rm pegi3s/coral`.

# Test data
To test the previous command, you can download and decompress [this FASTA compressed file](https://www.cs.helsinki.fi/u/lmsalmel/coral/basespace12x3.fasta.zip) (20MB).

Then, in the previous command you just need to replace `/data/input.fasta` with `/data/basespace12x3.fasta`.

# Using the coral image in Windows

Please, note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/coral -f /data/input.fasta -o /data/output.fasta`
