# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [AEGeAn](https://aegean.readthedocs.io/en/stable/), a toolkit for integrated genome analyses. Four programs are available under `AEGeAn`, namely `ParsEval` (for comparing two sets of gene annotations for the same sequence), `CanonGFF3` (for pre-processing GFF3 data encoding canonical protein-coding genes), `LocusPocus` (for computing interval loci (iLoci) from a provided set gene annotations), and `GAEVAL` (for computing coverage and integrity scores for gene models using transcript alignments).

# Using the AEGeAn image in Linux
You should adapt and run the following command: `docker run -v /your/data/dir:/data pegi3s/aegean bash -c "program_name <options>"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `reference_gff3` to the name of the GFF3 file containing the reference annotations.
- `prediction_gff3` to the name of the GFF3 file containing the prediction annotations.
- `results` to point to the file (under data) where results will be saved.

For instance, in order to run `ParsEval` (a program for comparing two sets of gene annotations for the same sequence) and saving the results in a file named `results`, you should run:
`docker run -v /your/data/dir:/data pegi3s/aegean bash -c "parseval /data/reference_gff3 /data/prediction_gff3 > /data/results"`

# Using the AEGeAn image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/aegean bash -c "parseval /data/reference_gff3 /data/prediction_gff3 > /data/results"`