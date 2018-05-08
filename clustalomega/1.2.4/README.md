# Using the Clustal Omega image
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/clustalomega -i /data/sequences.fasta -o /data/sequences_aligned.fasta`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `sequences.fasta` to the actual name of your FASTA file.
- `sequences_aligned.fasta` to the actual name of your aligned FASTA file.

To see the Clustal Omega help, just run `docker run --rm pegi3s/clustalomega --help`.
