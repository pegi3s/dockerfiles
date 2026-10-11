# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [AGAT](https://github.com/NBISweden/AGAT), a GFF/GTF annotation handling toolkit.

# Using the AGAT image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/agat agat_convert_sp_gxf2gxf.pl -g /data/gffFile -o /data/output.gff3`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `agat_convert_sp_gxf2gxf.pl` to the actual agat command you want to run.
- `gffFile` to the actual name of your GTF/GFF file.
- `output.gff3` to the actual name of your output file.

To see the [AGAT](https://nbisweden.github.io/AGAT/) help, just run `docker run --rm pegi3s/agat agat --help`.
