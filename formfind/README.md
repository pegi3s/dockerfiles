# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

This image facilitates the usage of [FormFind](https://github.com/VR51/formfind), a script that gets an HTML page on stdin and presents form information on stdout.

# Using the FormFind image in Linux
To extract the information from a specific bioinformatics web server, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/formfind bash -c "/opt/run <website-URL>"`

*Note*: The form information is stored on a file called `info` at the `/data` directory.

In this command, you should replace:
- `/your/data/dir` to point to the directory where output files will be created.
- `<website-URL>`to the URL address of the website you want to extract the information.

Please note that the default output directory is `/data`. 
If you want the output directory to have a different name you have to declare it at the end of the run command. 

For instance, if you want your output directory to be named `my_dir`, you should run: `docker run --rm -v /your/data/dir:/my_dir pegi3s/formfind bash -c "/opt/run <website-URL> /my_dir"`