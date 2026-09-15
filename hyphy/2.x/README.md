# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HyPhy](https://www.hyphy.org/) (Hypothesis Testing using Phylogenies), an open-source software package for the analysis of genetic sequences using techniques in phylogenetics, molecular evolution and machine learning.

Starting with HyPhy 2.5, analyses are run through the `hyphy` executable. The available standard analyses include `absrel`, `bgm`, `busted`, `fade`, `fel`, `fubar`, `gard`, `meme`, `relax` and `slac`.

# Using the HyPhy image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/hyphy hyphy <analysis> --alignment /data/inputFile --output /data/output/out.json`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<analysis>` to the name of the analysis you want to run (e.g. `fel`, `fubar`).
- `inputFile` to the actual name of your input alignment file.
- `out.json` to the actual name of your output file.

To list the available analyses and their options, run `docker run --rm pegi3s/hyphy hyphy -h` and `docker run --rm pegi3s/hyphy hyphy <analysis> --help`. HyPhy also provides an interactive mode: `docker run --rm -it pegi3s/hyphy hyphy -i`.

# Test data

To test the previous command, you can use the example datasets provided [here](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/input_test_data/hyphy.zip). After uncompressing the downloaded file, you should replace `/your/data/dir` by the actual working directory and run, for example:

```
docker run --rm -v /your/data/dir:/data pegi3s/hyphy hyphy fel --alignment /data/tutorial_data/lysin.fna --output /data/out.json
```

In the end, a JSON file with the results is generated.

# Using the HyPhy image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/hyphy hyphy <analysis> --alignment /data/inputFile --output /data/output/out.json`
