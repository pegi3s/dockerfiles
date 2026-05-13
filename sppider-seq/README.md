# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [sppiderseq](https://github.com/aporollo-lab/SPPIDER-seq), SPPIDER-seq predicts protein-protein interaction interface residues from query and partner protein sequences using partner-aware deep learning models.

# Using the sppiderseq image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/sppiderseq --query /data/query.fasta --partner /data/partner.fasta --output /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the local directory containing the query and partner FASTA files. The prediction results will be written to the selected output directory.
- `query.fasta and partner.fasta` to the actual name of your input protein sequence files in FASTA format, one for the query protein and one for the interaction partner protein.
- `interface_residues.csv` to the actual name of your CSV file containing residue-level SPPIDER-seq predictions for the query sequence against the partner sequence. The output directory also contains the original query_as_receptor and query_as_peptide prediction files.

To see the [sppiderseq](https://github.com/aporollo-lab/SPPIDER-seq) help, just run:
`docker run --rm pegi3s/sppiderseq --help`
