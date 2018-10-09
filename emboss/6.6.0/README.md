# (Please note that the original software licenses still apply)

This image allows the usage of the [`EMBOSS`](http://emboss.sourceforge.net) suite. Popular applications in this suite [are](http://emboss.sourceforge.net/what/#Overview):
- getorf: Find and extract open reading frames.
- prophet: Gapped alignment for profiles.
- infoseq: Displays some simple information about sequences.
- water: Smith-Waterman local alignment.
- pepstats: Protein statistics.
- showfeat: Show features of a sequence.
- palindrome: Looks for inverted repeats in a nucleotide sequence.
- eprimer3: Picks PCR primers and hybridization oligos.
- profit: Scan a sequence or database with a matrix or profile.
- extractseq: Extract regions from a sequence.
- marscan: Finds MAR/SAR sites in nucleic sequences.
- tfscan: Scans DNA sequences for transcription factors.
- patmatmotifs: Compares a protein sequence to the PROSITE motif database.
- showdb: Displays information on the currently available databases.
- wossname: Finds programs by keywords in their one-line documentation.
- abiview: Reads ABI file and display the trace.
- tranalign: Align nucleic coding regions given the aligned proteins.

To obtain the help of an application, you just need to run: `docker run --rm pegi3s/emboss <emboss-application-name> -h` (e.g. `docker run --rm pegi3s/emboss prophet -h`)

# Using the emboss image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/emboss <emboss-application-name> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<emboss-application-name>` to the name of the `EMBOSS` application you want to use.
- `<options>` with the specific options of the `EMBOSS` application. These options will include the input/output files, which should be referenced under `/data/`.

# Using the emboss image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/emboss <emboss-application-name> <options>`
