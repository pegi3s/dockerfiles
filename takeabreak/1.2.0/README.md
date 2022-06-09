# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TakeABreak](https://github.com/GATB/TakeABreak/blob/master/README.md), a tool that detects inversion breakpoints directly from NGS (Next Generation Sequencing) reads, without the use of any reference genome and without the "reassembly" of the genomes.

# Using the TakeABreak image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/takeabreak bash -c "./TakeABreak -in /data/test_reads.fasta,/data/reference_reads.fasta -out /data/output"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `/test_reads.fasta` to the test reads you want to use.
- `/reference_reads.fasta` to the file containing the reference reads you want to use.
- `/data/output` to the actual name of your output files (.fasta and .h5).

### *Note 1*
The input reads files can be FASTA, FASTQ or GZIPPED.

To see the `TakeABreak` help, just run `docker run --rm pegi3s/takeabreak TakeABreak -help`.

# Test data

To test the previous commands, you can use two input FASTA files, containing the test reads and the reference reads, available [here](https://github.com/pegi3s/dockerfiles/tree/master/takeabreak/1.2.0/test_data/toy_example_reads.fasta) and [here](https://github.com/pegi3s/dockerfiles/tree/master/takeabreak/1.2.0/test_data/toy_example_with_inv_reads.fasta).

Then, you should simply run: `docker run --rm -v /your/data/dir:/data pegi3s/takeabreak bash -c "./TakeABreak -in /data/toy_example_reads.fasta,/data/toy_example_with_inv_reads.fasta -out /data/output"`

### *Note 2*
The previous command generates two files:
- `.h5`: a Graph file in binary format.
- `.fasta`: a FASTA file containing the canonical representations of the detected inversion breakpoints.

### *Note 3*
Each inversion corresponds to four entries in the FASTA file:
- The first two correspond to the breakpoint sequences that should be present in one genome `(a-u,v-b)`.
- The last two are the corresponding breakpoint sequences in the other genome `(a-revcomp(v),revcomp(u)-b)`.

# Using the TakeABreak image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/takeabreak bash -c "./TakeABreak -in /data/test_reads.fasta,/data/reference_reads.fasta -out /data/output"`
