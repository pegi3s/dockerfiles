# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [kentUtils](https://github.com/ENCODE-DCC/kentUtils), a genome data utilities suite.

# Using the kentUtils image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/kentutils faToTwoBit /data/fastaFile /data/output.2bit`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `faToTwoBit` to the name of the kentUtils utility you want to use (e.g. `twoBitToFa`, `faSize`, `faSplit`, `bedToBigBed`).
- `fastaFile` to the actual name of your FASTA file.
- `output.2bit` to the actual name of your output file.

To see the kentUtils help, just run `docker run --rm pegi3s/kentutils faToTwoBit` (without arguments) or `docker run --rm pegi3s/kentutils faToTwoBit -h`.
