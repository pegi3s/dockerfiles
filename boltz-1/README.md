# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Boltz-1](https://github.com/jwohlwend/boltz), a deep learning-based tool for predicting the 3D structure of proteins and biomolecular complexes from amino acid sequences.

# Using the Boltz-1 image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/boltz-1 bash -c "boltz predict /data/input.fas --accelerator cpu --cache /data/.boltz --out_dir /data/output/"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input FASTA file with the protein sequence.
- `input.fas` to the actual name of your input sequence file in FASTA format.
- `output` to the actual name of your directory where the predicted structure and results will be saved.

To see the [Boltz-1](https://github.com/jwohlwend/boltz) help, just run:
`docker run --rm pegi3s/boltz-1 boltz --help`
