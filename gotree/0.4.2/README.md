# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of [Gotree](https://github.com/evolbioinfo/gotree), a set of command line tools to manipulate phylogenetic trees.

By running the command `docker run --rm pegi3s/gotree gotree help` you can list the commands included in Gotree.

To obtain the help of a particular application, you just need to run: `docker run --rm pegi3s/gotree gotree <gotree-application-name> -h` (e.g. `docker run --rm pegi3s/gotree gotree matrix -h`)

# Using the Gotree image in Linux

To run an application, you should adapt and run the following command: `docker run -v /your/data/dir:/data --rm pegi3s/gotree gotree <gotree-application-name> -i /data/input -o /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<gotree-application-name>` to the name of the `Gotree` application you want to use.
- `<input>` to the actual name of your input file.
- `out` to the actual name of your output file.

For instance, to use the `matrix` application, you should run: `docker run -v /your/data/dir:/data --rm pegi3s/gotree gotree matrix -i /data/example.nwk -o /data/output`

A sample `example.nwk` file can be: 

```
(B:6.0,(A:5.0,C:3.0,E:4.0)Ancestor1:5.0,D:11.0);
``` 

# Using the Gotree image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/gotree gotree <gotree-application-name> -i /data/input -o /data/output`
