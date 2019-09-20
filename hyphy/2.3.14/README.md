# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HyPhy](https://stevenweaver.github.io/hyphy-site/) (Hypothesis Testing using Phylogenies), an open-source software package for the analysis of genetic sequences using techniques in phylogenetics, molecular evolution and machine learning.

# Using the HyPhy image in Linux
You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/hyphy HYPHYMP`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.

*Note*: After executing the previous command, a set of questions will be presented to you in order to define the experiment's parameters.

To see the `HyPhy` help, just run `docker run --rm pegi3s/hyphy HYPHYMP -h`.

# Test data
To test the previous command, you can use as input some example datasets provided [here](https://github.com/veg/hyphy-site/blob/master/docs/tutorials/files/tutorial_data.zip?raw=true) (12MB). Make sure you prepare your input data as described [here](http://hyphy.org/tutorials/CL-prompt-tutorial/) in the section `Preparing input data for HyPhy`.

For instance, to run `FUBAR` you should follow these steps:

- Run `docker run --rm -it -v /your/data/dir:/data pegi3s/hyphy HYPHYMP`
- Type `1` for Selection Analyses
- Type `4` for `FUBAR`
- Type `1` for Universal Genetic Code
- Select a coding sequence alignment file: `/data/hiv1_transmission.fna`
- Type `y` to use the tree found in the data file

In the end it generates a table with the sites subject to diversifying positive selection.

# Using the HyPhy image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/hyphy HYPHYMP`
