# (Please note that the original software licenses still apply)

This image facilitates the usage of [`BLAST`](https://blast.ncbi.nlm.nih.gov/Blast.cgi), a program that finds regions of similarity between biological sequences. It compares nucleotide or protein sequences to sequence databases and calculates the statistical significance.

# Using BLAST image in Linux

In order to use this image you need to create a custom database from a multi-FASTA file of sequences with this command: `docker run --rm -v /your/data/dir:/data pegi3s/blast makeblastdb –in /data/mydb.fasta –dbtype nucl –parse_seqids`

See the following section, [`Building a BLAST database with local sequences`](https://www.ncbi.nlm.nih.gov/books/NBK279688/), for more details.

After the creation of the database, in order to execute a `blastn` for instance, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/blast blastn -query /data/input -db /data/mydb.fasta -evalue 0.05 -num_descriptions 500000 -num_alignments 500000 -outfmt 3 -out /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the query file you want to execute.
- `input` to the actual name of your query file.
- `mydb.fasta` to the actual name of the database you created.
- `output` to the actual name of your output file.

For other options common to all BLAST search applications please go [here](https://www.ncbi.nlm.nih.gov/books/NBK279684/).

*Note*: The parameter `max_target_seqs` does not behave as it is described. Please read the following [article](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/bty833/5106166).

To obtain abbreviated help of an application, you just need to run: `docker run --rm pegi3s/blast <blast-application-name> -h` (e.g. `docker run --rm pegi3s/blast blastn -h`). For more extensive documention just replace the `-h` flag for the `-help` flag. 

# Using BLAST image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

In order to use this image you need to create a custom database from a multi-FASTA file of sequences with this command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/blast makeblastdb –in /data/mydb.fasta –dbtype nucl –parse_seqids`

See the following section, [`Building a BLAST database with local sequences`](https://www.ncbi.nlm.nih.gov/books/NBK279688/), for more details.

After the creation of the database, in order to execute a `blastn` for instance, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/blast blastn -query /data/input -db /data/mydb.fasta -evalue 0.05 -num_descriptions 500000 -num_alignments 500000 -outfmt 3 -out /data/output`
