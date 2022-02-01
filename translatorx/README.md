# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TranslatorX](http://translatorx.co.uk/), a tool to perform a nucleotide sequence alignment using a protein sequence alignment as a guide. It also performs protein alignments and alignment cleaning based on amino acid information.

# Using the TranslatorX image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/opt pegi3s/translatorx bash -c "perl translatorx_vLocal.pl -i input.fas -a alignment.fas -o output"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to align.
- `input.fas` to the actual name of your FASTA input file containing the nucleotide sequences.
- `alignment.fas` to the actual name of your FASTA input file containing the protein sequence alignment.
- `output` to the actual name of your output file.

To see the `TranslatorX` help, just run: `docker run --rm -v /your/data/dir:/opt pegi3s/translatorx bash -c "perl translatorx_vLocal.pl -help"`

### *Note*

Severall output files are produced by `TranslatorX` but the one with the desired result is `output.nt_ali.fasta`

# Using the TranslatorX image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: 
`docker run --rm -v "/c/Users/User_name/dir/":/opt pegi3s/translatorx bash -c "perl translatorx_vLocal.pl -i input.fas -a alignment.fas -o output"`
