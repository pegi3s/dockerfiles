# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Wgsim](https://github.com/lh3/wgsim), a small tool for simulating sequence reads from a reference genome. It is able to simulate diploid genomes with `SNPs` and insertion/deletion (`INDEL`) polymorphisms, and simulate reads with uniform substitution sequencing errors. It does not generate `INDEL` sequencing errors, but this can be partly compensated by simulating `INDEL` polymorphisms.

`Wgsim` outputs the simulated polymorphisms, and writes the true read coordinates as well as the number of polymorphisms and sequencing errors in read names. One can evaluate the accuracy of a mapper or a `SNP` caller with `wgsim_eval.pl` that comes with the package.

To see `Wgsim` options, just run `docker run --rm pegi3s/wgsim wgsim -h`.

# Using the Wgsim image in Linux

You should adapt and run the following command: `docker run --rm -v "/your/data/dir:/data" pegi3s/wgsim wgsim <options> <in.ref.fa> <out.read1.fq> <out.read2.fq>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to analyze.
- `<options>` with the specific options of the `Wgsim` tool. These options will include the input/output files, which should be referenced under `/data/`.
- `<in.ref.fa>` to the actual name of your input FASTA file.
- `<out.read1.fq>` to the actual name of your output reads file 1 in FASTQ format.
- `<out.read2.fq>` to the actual name of your output reads file 2 in FASTQ format.

For instance, if you want to generate simulated reads from `chr19_KI270866v1_alt.fasta`, you should run: `docker run --rm -v "/your/data/dir:/data" pegi3s/wgsim wgsim -1151 -2151 -d500 -r0 -e0 -N10000 -R0 -X0 /data/chr19_KI270866v1_alt.fasta /data/7859_GPI.read1.fq /data/7859_GPI.read2.fq`

### *Note*
The previous command generates two FASTQ files, `7859_GPI.read1.fq` and `7859_GPI.read2.fq`, one for each mate of the paired reads.

- Each read is 151 bases. Set with `-1151` and `-2151` for read1 and read2, respectively.
- The outer distance or insert size is 500 bases with a standard deviation of 50. This is set with the `-d500` parameter.
- The files contain 10K read pairs, and this is set by the `-N10000` parameter.
- None of the reads contain indels (`-R0` & `-X0`) nor mutations/variants (`-r0`).
- Base quality scales with the value given to `-e` so we set it to zero (`-e0`) for base quality scores of `I`, which is, according to [this page](https://en.wikipedia.org/wiki/FASTQ_format) and [this site](http://broadinstitute.github.io/picard/explain-qualities.html), an excellent base quality score equivalent to a Sanger Phred+33 score of 40.

For a 43 kb contig, 10K x 2 x 151 reads should give you ~70x hypothetical coverage.

# Test data
To test the previous command, the input FASTA file used is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/wgsim/0.3.0/test_data/chr19_KI270866v1_alt.fasta).

# Using the Wgsim image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/wgsim wgsim <options> <in.ref.fa> <out.read1.fq> <out.read2.fq>`
