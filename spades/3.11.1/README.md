# (Please note that the original software licenses still apply)

# Using the SPAdes image in Linux

The [`SPAdes`](http://cab.spbu.ru/software/spades/) manual can be found [here](http://spades.bioinf.spbau.ru/release3.11.1/manual.html). This image allows you to use the main `SPAdes` scripts, namely:
- `spades.py` (main executable script)
- `dipspades.py` (main executable script for dipSPAdes)
- `metaspades.py` (main executable script for metaSPAdes)
- `plasmidspades.py` (main executable script for plasmidSPAdes)
- `rnaspades.py` (main executable script for rnaSPAdes)
- `truspades.py` (main executable script for truSPAdes)

For instance, you can show the help associated to the `spades.py` main script by running: `docker run --rm pegi3s/spades spades.py --help`

To run this main script, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/spades spades.py [options] -o /data`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `data` to the actual results directory.
- `[options]` with the input data and other parameters. Refer to the [SPAdes manual](http://spades.bioinf.spbau.ru/release3.11.1/manual.html#sec3.2) to know how this information should be given.

# Test data

To test `SPAdes` you can download these two *E. coli* FASTQ files from the [examples](http://cab.spbu.ru/software/spades/#examples): [left](http://spades.bioinf.spbau.ru/spades_test_datasets/ecoli_mc/s_6_1.fastq.gz) and [right](http://spades.bioinf.spbau.ru/spades_test_datasets/ecoli_mc/s_6_2.fastq.gz)

Then, you can run the main script by adapting the following command: `docker run --rm -v /your/data/dir:/data pegi3s/spades spades.py --careful --only-assembler --pe1-1 /data/s_6_1.fastq.gz --pe1-2 /data/s_6_2.fastq.gz -o /data/output`

Note that `/your/data/dir` should point to the directory that contains the input files you have downloaded. The output files will be created in the `/data/output` directory.  You can also speed up the execution by adding `-t 4` to tell `SPAdes` to use 4 threads.

*Note*: the analysis of this files may take a while. For instance, it took 100 minutes to complete using 4 threads on a Ubuntu 14.04.3 LTS with an Intel(R) Core(TM) i5 @ 2.20GHz processor, 16GB of RAM and SSD disk.

# Using the SPAdes image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

To analyze the test data, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/spades spades.py --careful --only-assembler --pe1-1 /data/s_6_1.fastq.gz --pe1-2 /data/s_6_2.fastq.gz -o /data/output`
