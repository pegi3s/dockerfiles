# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [make_lastz_chains](https://github.com/hillerlab/make_lastz_chains), a pairwise genome alignment pipeline.

# Using the make_lastz_chains image in Linux

This Nextflow pipeline runs every step inside the `ghcr.io/hillerlab/make_lastz_chains` container, so the Docker socket must be mounted and the working directory shared with the host. You should adapt and run the following command: `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data -w /your/data/dir pegi3s/make_lastz_chains nextflow run /opt/make_lastz_chains/main.nf -params-file /opt/make_lastz_chains/params.json -profile docker --reference_name ref_name --query_name query_name --reference_genome /data/reference.fasta --query_genome /data/query.fasta --outdir /data/results`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `ref_name` and `query_name` to the names used to label the reference and query genomes.
- `reference.fasta` and `query.fasta` to the actual names of your softmasked genome FASTA files.
- `results` to the output directory where the chain files will be created.

Note that the genomes must be softmasked (lowercase, not hardmasked) and scaffold names must not contain spaces or dots (e.g. rename `NC_00000.1` to `NC_00000`). The final chains are written to `<outdir>/07_final`.

To see the [make_lastz_chains](https://github.com/hillerlab/make_lastz_chains) help, just run `docker run --rm pegi3s/make_lastz_chains nextflow run /opt/make_lastz_chains/main.nf -help`.
