# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [KaKs Calculator](https://ngdc.cncb.ac.cn/tools/kaks), a toolbox that calculates nonsynonymous (`Ka`) and synonymous (`Ks`) substitution rates by means of various models or model selection and averaging.

# Using the KaKs Calculator image in Linux

You should adapt and run the following commands:

- starting from FASTA file: `docker run --rm -v /your/data/dir:/data pegi3s/kakscalculator bash -c "FASTA-AXT /data/input.fa && KaKs_Calculator -i /data/input.fa.axt -o /data/result.axt.kaks"`
  
- starting from AXT file: `docker run --rm -v /your/data/dir:/data pegi3s/kakscalculator bash -c "KaKs_Calculator -i /data/input.axt -o /data/result.axt.kaks"`

In this commands, you should replace:

- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `input.fa` to the actual name of your input file with the aligned CDS sequences (with no sequence line breaks) in FASTA format. The first nucleotide must correspond to the first codon position.
- `input.axt` to the actual name of your input file with the aligned CDS sequences in AXT format. The first nucleotide must correspond to the first codon position.

To see the `KaKs Calculator` help, just run `docker run --rm pegi3s/kakscalculator bash -c "KaKs_Calculator -h"`.

# Test data

To test the previous commands, the input FASTA file used is available [here](https://github.com/pegi3s/dockerfiles/tree/master/kakscalculator/2.0/test_data/example.fa).

Then, you should simply run: `docker run --rm -v /your/data/dir:/data pegi3s/kakscalculator bash -c "FASTA-AXT /data/example.fa && KaKs_Calculator -i /data/example.fa.axt -o /data/example_result.axt.kaks"`

# Using the KaKs Calculator image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/kakscalculator bash -c "FASTA-AXT /data/input.fa && KaKs_Calculator -i /data/input.fa.axt -o /data/result.axt.kaks"`

### *Note*
In order to compile the `KaKs Calculator` software for Ubuntu, the following change was performed to the original file:

- added `#include <string.h>` to the top of `base.h`.
