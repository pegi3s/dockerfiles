# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ProSplign/ProCompart](https://www.ncbi.nlm.nih.gov/sutils/splign/splign.cgi), a global alignment tool to produce accurate spliced alignments and to compute alignments of distantly related proteins with low similarity. More specifically, this image provides a script that executes the ProSplign/ProCompart pipeline as implemented in our [SEDA tool](https://www.sing-group.org/seda/manual/operations.html#prosplign-procompart-pipeline).

Section 3.6 of [this paper](https://doi.org/10.1109/TCBB.2020.3040383) about SEDA describes the pipeline. This pipeline receives as input two FASTA files: a target FASTA (a nucleotide genome) used as subject and another one (a protein CDS) used as query, and performs the following steps:
ssion.ion applies the following steps:
1. Create a BLAST database for the nucleotide subject file.
2. Run a tblastn using the protein query file against the subject database, sorting the output by subject and query.
3. Run ProCompart to find the approximate locations of the protein instances on the nucleic acid sequences.
4. Run ProSplign using the compartment file generated in the previous step and the two FASTA files as input to generate an alignment for each
compartment.
5. Extract the sequences from the alignments file in order to create the output FASTA file with the annotations.

# Using ProSplign/ProCompart image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/prosplign-procompart prosplign-procompart-pipeline /data/<nucleotide_subject> /data/<query_protein_CDS> /data/<output> [<max_target_seqs>]`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<nucleotide_subject>` to the name of the FASTA file for the target FASTA.
- `<query_protein_CDS>` to the name of the protein FASTA file for the CDS query.
- `<output>` to the name of the output FASTA file.

Note that the `<max_target_seqs>` is optional. It specifies the value for the `-max_target_seqs` parameter of the `tblastn` command. If not provided, the default value is `1`.

# Test data

To test the these commands, it is possible to use [this test data](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/prosplign-procompart/test-data-prosplign-procompart.zip) to apply the protocol described in [this page of ProSplign/ProCompart](https://www.ncbi.nlm.nih.gov/sutils/static/prosplign/prosplign.html).

After downloading and unzipping the test data, you should simply run (remember to change the `/your/data/dir` path):

```bash
docker run --rm -v /your/data/dir:/data pegi3s/prosplign-procompart prosplign-procompart-pipeline /data/Demo_Genome_Nucleotides.fa /data/Demo_Query_Protein.fa /data/output.fasta
```

# Using ProSplign/ProCompart image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/prosplign-procompart /data/<nucleotide_subject> /data/<query_protein_CDS> /data/<output> [<max_target_seqs>]`
