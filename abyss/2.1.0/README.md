This image facilitates the usage of [`ABySS`](https://github.com/bcgsc/abyss), a de novo sequence assembler intended for short paired-end reads and large genomes. All `abyss-*` commands are available in the path. For instance, you can show the `abyss-pe` help by running `docker run --rm pegi3s/abyss abyss-pe -h`.

# Available images
Since the default k-mer size to run an assembly is 64, we have compiled two additional images with `--enable-maxk=128` and `--enable-maxk=256`. Have a look at the `Tags` tab of the Docker Hub repository in order to choose the most appropiate one.

*Note*: increasing `--enable-maxk` increases the memory requirements of `ABySS` and you may need to adjust some MPI settings for large k-mer sizes, as described [here](https://github.com/bcgsc/abyss/wiki/ABySS-Users-FAQ#2-my-abyss-assembly-jobs-hang-when-i-run-them-with-high-k-values-eg-k250). 

# Using the ABySS image: assemble a small synthetic data set

To test `ABySS`, you can download and uncompress the test dataset available [here](http://www.bcgsc.ca/platform/bioinfo/software/abyss/releases/1.3.4/test-data.tar.gz).

Then, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/abyss abyss-pe k=25 name=test in='/data/test-data/reads1.fastq /data/test-data/reads2.fastq' --directory=/data/results`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `results` to point to the directory (under `data`) where results will be generated. Note that this directory must exist before running the analysis as `ABySS` won't create it.

# Using the ABySS image in Windows

Please, note that data must be under in the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permisions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/abyss abyss-pe k=25 name=test in='/data/test-data/reads1.fastq /data/test-data/reads2.fastq' --directory=/data/results`
