# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HTSeq](https://htseq.readthedocs.io/en/latest/), a Python package for analysis of high-throughput sequencing data.

# Using the HTSeq image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/htseq <script-name> [script arguments]`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `<script-name>` to the actual name of the script to be executed (e.g. `htseq-qa` or `htseq-count`.
- `[script arguments]` with the argumetns required by the script.

# Using the HTSeq image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/htseq <script-name> [script arguments]`

docker run --rm -v "$(pwd):$(pwd)" -w "$(pwd)" pegi3s/htseq:0.12.3 htseq-count --format bam --order pos --mode intersection-strict --stranded reverse --minaqual 1 --type exon --idattr gene_id hcc1395_normal_rep1.bam Homo_sapiens.GRCh38.86.chromosome22.gtf > test.out

docker run --rm -v "$(pwd):$(pwd)" -w "$(pwd)" singgroup/dewe:1.3 /opt/HTSeq-0.12.3/scripts/htseq-count --format bam --order pos --mode intersection-strict --stranded reverse --minaqual 1 --type exon --idattr gene_id hcc1395_normal_rep1.bam Homo_sapiens.GRCh38.86.chromosome22.gtf > test.out
