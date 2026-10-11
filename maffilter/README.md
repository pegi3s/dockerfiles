# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MafFilter](https://github.com/jydu/maffilter), a multiple genome alignment files processor.

# Using the MafFilter image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/maffilter input.file=/data/mafFile input.file.compression=none input.format=Maf output.log=/data/out_name.log "maf.filter=XFullGap(species=(hg18, panTro1, baboon, mm4, rn3)), Output(file=/data/filtered.maf)"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `mafFile` to the actual name of your MAF alignment file.
- `output/out_name.log` to the actual name of your output file.
- `XFullGap(...)` to the MafFilter filter(s) you want to apply.
- `filtered.maf` to the actual name of your output file.

To see the [MafFilter](https://github.com/jydu/maffilter) help, just run `docker run --rm pegi3s/maffilter`.
