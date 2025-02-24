# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the creation of customized Dockerfiles for building R-based images with system-level dependencies and R packages installed.

# Using the `r_builder` image in Linux

You should adapt and run the following command: `docker run -u "$(id -u):$(id -g)" --rm -v /var/run/docker.sock:/var/run/docker.sock -v "/your/data/dir:/data" -w /data pegi3s/r_builder generate_dockerfile.sh config.json`

In this command, you should replace `/your/data/dir` to point to the directory that contains the `config.json` file, that specifies the image dependencies and packages in a JSON file like the following:

```json
{
  "name": "my_r_image_with_sva",
  "image_version": "4.4.0",
  "from": "r-base:4.4.0",
  "packages": {
    "apt": ["libssl-dev", "libcurl4-openssl-dev", "libxml2-dev"],
    "r": ["ggplot2"],
    "biocmanager": ["sva"]
  }
}
```

The script will create a folder named `<name>_<image_version>` with a `Dockerfile` and build the image automatically.
