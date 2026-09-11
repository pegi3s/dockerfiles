# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Haplogrep](https://haplogrep.readthedocs.io/en/latest/), a fast and free haplogroup classification tool.

# Using the Haplogrep image in Linux
You should adapt and run the following command:

`docker run --rm -v /your/data/dir:/data pegi3s/haplogrep classify --input=/data/input --tree=phylotree-rcrs@17.2 --out data/out.txt`

In this command you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to analyze.
- `input` to the actual name of your input file.
- `out.txt` to the desired name of the output file.

- You may also want to replace `phylotree-rcrs@17.2` for another reference sequence.

To see the `haplogrep` help, just run `docker run --rm pegi3s/haplogrep --help`.
