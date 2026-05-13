# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ispip](https://github.com/eved1018/ISPIP), ISPIP integrates protein-protein interface prediction scores from external tools to generate interface residue prediction models and predictions.

# Using the ispip image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/ispip -i /data/input.csv -of /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the local directory containing the input CSV file. The generated model files and prediction results will be written to the selected output directory.
- `input.csv` to the actual name of your input CSV file containing the columns expected by ISPIP, including precomputed prediction scores from external tools such as PredUs, ISPred and DockPred, together with annotated interface labels. The included test CSV is synthetic and is intended only to validate execution of the Docker workflow.
- `ispip_pipeline_done.txt` to the actual name of your marker file indicating that the full ISPIP workflow completed successfully. The output directory also contains generated .joblib model files and prediction outputs.

To see the [ispip](https://github.com/eved1018/ISPIP) help, just run:
`docker run --rm pegi3s/ispip --help`
