# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [matplotlib-venn](https://github.com/konstantint/matplotlib-venn), a creation of Venn and Euler plots.

# Using the matplotlib-venn image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/matplotlib-venn python3 /data/python_script.py`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file(s).
- `python_script.py` to the actual name of your Python script file.

To see the [matplotlib-venn](https://github.com/konstantint/matplotlib-venn) help, just run `docker run --rm pegi3s/matplotlib-venn python3 -c "help('matplotlib_venn')"`.
