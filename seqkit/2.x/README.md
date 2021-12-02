# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [SeqKit](https://github.com/shenwei356/seqkit/blob/master/README.md) suite - a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. Frequently used tools in this suite [are](https://bioinf.shenwei.me/seqkit/usage/):

- Sequence and subsequence:

	- seq
	- subseq
	- sliding
	- stats
	- faidx
	- watch
	- sana

- Format conversion:

	- fq2fa
	- fx2tab & tab2fx
	- convert
	- translate

- Searching:

	- grep
	- locate
	- fish
	- amplicon

- BAM processing and monitoring

	- bam 

- Set Operations:

	- head
	- range
	- sample
	- rmdup
	- duplicate
	- common
	- split
	- split2

- Edit:

	- replace
	- rename
	- restart
	- concat
	- mutate

- Ordering:

	- shuffle
	- sort

- Misc:

	- genautocomplete

To obtain the help of an application, you just need to run: `docker run --rm pegi3s/seqkit <seqkit-application-name> --help` (e.g. `docker run --rm pegi3s/seqkit subseq --help`)

# Using the SeqKit image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/seqkit <seqkit-application-name> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<seqkit-application-name>` to the name of the `SeqKit` application you want to use.
- `<options>` with the specific options of the `SeqKit` application. These options will include the input/output files, which should be referenced under `/data/`.

# Using the SeqKit image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/seqkit <seqkit-application-name> <options>`
