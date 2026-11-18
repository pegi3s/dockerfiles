# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [BUSCO](https://gitlab.com/ezlab/busco), a genome assembly completeness assessment tool.

# Using the BUSCO image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/busco busco -i /data/fastaFile -m genome -l bacteria_odb10 -o busco_output --out_path /data/output --cpu 8`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `fastaFile` to the actual name of your input FASTA file.
- `-m genome` to the analysis mode (`genome`, `proteins` or `transcriptome`).
- `bacteria_odb10` to the name of the lineage dataset to use (it is downloaded automatically if not available locally).
- `busco_output` to the actual name of your output folder.
- `output` to the directory where the output folder will be created.
- `8` after `--cpu` to the actual number of CPUs to use.

To see the [BUSCO](https://busco.ezlab.org/busco_userguide.html) help, just run `docker run --rm pegi3s/busco busco -h`.
