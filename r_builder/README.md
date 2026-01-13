# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the creation of customized Dockerfiles for building R-based images with system-level dependencies and R packages installed.

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the `pegi3s/r_builder:1.2.1-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `pegi3s/r_builder:1.2.1` tag. Starting with version `pegi3s/r_builder:1.2.1-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

# Using the `r_builder` image in Linux

You should adapt and run the following command: `docker run -u "$(id -u):$(id -g)" --group-add $(getent group docker | cut -d: -f3) --rm -v /var/run/docker.sock:/var/run/docker.sock -v "/your/data/dir:/data" -w /data pegi3s/r_builder generate_dockerfile.sh config.json`

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
