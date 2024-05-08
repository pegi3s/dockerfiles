# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [pycision](https://github.com/Ahhgust/Pycision/), a custom tool for trimming primer sequences in Ion Torrent reads from the Precision ID mtDNA panel.

# Using the pycision image in Linux
You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/pycision data/input2.bed data/input1.bam`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the BAM file you want to process.
- `input1.bam` to the actual name of your input bam file.
- `input2.bed` to the actual name of your input bed file.

Pycision will output three files in the same directory as your input file:
- `input1.softClipped.bam`: raw output
- `input1.softClipped.sorted.bam`: sorted output
- `input1.softClipped.sorted.bam.bai`: index for the sorted output

Take into account that if you use the  -f/--fifty_percent option outputs will look like this:
- `input1.softClipped.halfway.bam`: raw output
- `input1.softClipped.halfway.sorted.bam`: sorted output
- `input1.softClipped.halfway.sorted.bam.bai`: index for the sorted output

To see the `pycision` help, just run `docker run --rm pegi3s/pycision`

Apart from the two bed files included with pycision by default, this image has three extra beds which are essential to run the [precision caller pipeline](https://github.com/filcfig/PCP):
- `1_exceptfirst.bed`: contains all the amplicons apart from the starting and end positions (15-16569)
- `2_wholemt162.bed`: contains the last amplicon (16541-16649)
- `3_firstonly.bed`: contains the first amplicon (0-80)

Remember you can also use your own bed files.

