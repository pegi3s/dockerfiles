# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of **Rtn** ([github](https://github.com/Ahhgust/RtN)) ([publication](https://doi.org/10.1093/bioinformatics/btaa642)), a NUMT removal tool.

# Using the RtN image in Linux
You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/rtn -h RtN/humans.fa -n RtN/Calabrese_Dayama_Smart_Numts.fa -b ./data/input.bam`

# Ion Torrent data
For Ion Torrent data it is reccomended to use the -i flag in order to not take into account indels in the likelyhood function (see rtn docs).

`docker run --rm -v /your/data/dir:/data pegi3s/rtn -i -h RtN/humans.fa -n RtN/Calabrese_Dayama_Smart_Numts.fa -b ./data/input.bam`

In either of these commands, you should replace:
- `/your/data/dir` to point to the directory that contains the BAM file you want to process.
- `input.bam` to the actual name of your input bam file.

These commands generate a new BAM file in the same folder of the input file, named: `input.rtn.bam` which is the output of the NUMT removal process .

To see the `rtn` help, just run `docker run --rm pegi3s/rtn`

