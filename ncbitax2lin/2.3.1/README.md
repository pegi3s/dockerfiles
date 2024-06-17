# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [NCBItax2lin](https://github.com/zyxue/ncbitax2lin), a Python utility for convert the NCBI taxonomy dump into lineages.

# Using ncbitax2lin image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/ncbitax2lin ncbitax2lin --nodes-file /data/taxdump/nodes.dmp --names-file /data/taxdump/names.dmp --output /data/output.csv.gz`

In this command, you should replace `/your/data/dir` to point to the directory that contains the taxdump database files and where the output file will be created.

# Test data

To test the previous command, first download taxonomy dump from NCBI using the commands below and then run the command:

```bash
wget -N ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz
mkdir -p taxdump && tar zxf taxdump.tar.gz -C ./taxdump
```

# Using ncbitax2lin image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/ncbitax2lin ncbitax2lin --nodes-file /data/taxdump/nodes.dmp --names-file /data/taxdump/names.dmp --output /data/output.csv.gz`
