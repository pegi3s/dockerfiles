# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ispip](https://github.com/eved1018/ISPIP), ISPIP integrates protein-protein interface prediction scores from external tools to generate interface residue prediction models and predictions.

# Using the ispip image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/ispip -i /data/input.csv -of /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input CSV file.
- `input.csv` to the actual name of your input CSV file containing the columns expected by ISPIP, including precomputed prediction scores from external tools such as PredUs, ISPred and DockPred, together with annotated interface labels.
- `output` to the actual name of your output folder.

To see the [ispip](https://github.com/eved1018/ISPIP) help, just run:
`docker run --rm pegi3s/ispip --help`
