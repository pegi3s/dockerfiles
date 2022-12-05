# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the creation of a GFF3 file from a FASTA file containing CDS and a genome FASTA file.

# Using cds2gff3-maker image in Linux

You should adapt and run the following command:
```
docker run --rm -it -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir/data:/data pegi3s/cds2gff3-maker /data/CDS /data/genome /data/output.gff3
```

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to convert.
- `<CDS>` to the name of the CDS FASTA file.
- `<genome>` to the name of the genome FASTA file.
- `<output.gff3>` to the name of the output GFF3 file.

This script requires Docker since it runs scripts and commands from other images (`pegi3s/utilities` and `pegi3s/splign-compart`) to do its job. Thus, this script requires additional parameters in the `docker run` command to allow the docker container to run other containers using the host's docker:

- `-v /tmp:/tmp`: mounts the host's `/tmp` directory in the same path.
- `-v /var/run/docker.sock:/var/run/docker.sock`: mounts the `docker.sock` to give access to the host's docker.

By default, the scripts use the latest versions of those Docker images. To change them, add the following environment variables to the `docker run` command:
- `--env VERSION_PEGI3S_UTILITIES=0.22.0`.
- `--env VERSION_PEGI3S_SPLIGN_COMPART=1.2.1`.

# Test data

To test the `pegi3s/cds2gff3-maker` image, it is possible to use [this test data](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/cds2gff3-maker/test-data-cds2gff3-maker.zip). After downloading and unzipping the test data, you should simply run (remember to change the `/your/data/dir` path):

```
docker run --rm -it -v /tmp:/tmp -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir/data:/data pegi3s/cds2gff3-maker /data/CDS /data/genome /data/output.gff3
```

The ZIP also contains an example of the GFF3 file that should be obtained (`expected-output.gff3`).

# Changelog

The `latest` tag contains always the most recent version.

## [1.0.0] - 05/12/2022
- Initial version.
