# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [MultiQC](https://multiqc.info/) Python 3 package, a software tool for the summarization of results from bioinformatics analyses into a single report.

# Using the MultiQC image in Linux

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/multiqc python3 /data/script.py`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files or directories you want to analyze with the python script to be executed.
- `/data/script.py` to the actual name of your script using MultiQC (i.e. containing `import multiqc`).

# Using the MultiQC image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -it -v "/c/Users/User_name/dir/":/data pegi3s/multiqc python3 /data/script.py`
