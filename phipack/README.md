# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PhiPack](https://www.maths.otago.ac.nz/~dbryant/software/phimanual.pdf) software. `PhiPack` implements tests for recombination (`Pairwise Homoplasy Index (Phi)`, `Maximum χ2
(Max Chi^2)` and the `Neighbour Similarity Score (NSS)`), and can produce refined incompatibility matrices.

# Using the PhiPack image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/phipack bash -c "Phi -f /data/input.fasta -p 1000 -o > /data/output"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the aligned FASTA file you want to analyze.
- `input.fasta` to the actual name of your input file.
- `output` to the actual name of your output file.

To see the `PhiPack` help, just run `docker run --rm pegi3s/phipack Phi`.

# Using the PhiPack image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/phipack bash -c "Phi -f /data/input.fasta -p 1000 -o > /data/output"`
