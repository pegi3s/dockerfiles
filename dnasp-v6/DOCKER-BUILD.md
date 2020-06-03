# Building the DnaSP v6 Docker image

DnaSP v6 is a Windows application and it requires wine to run in a Linux-based Docker image. The `scottyhardy/docker-wine` Docker image was used as base image since it provides a complete wine installation. You can check this image at [Docker Hub](https://hub.docker.com/r/scottyhardy/docker-wine) and [GitHub](https://www.github.com/scottyhardy/docker-wine).

The steps to build the `pegi3s/dnasp-v6` Docker image are:

1. Place into this directory and run `docker build ./ -t pegi3s/dnasp-v6`. The Dockerfile [turns off wine debugging](https://askubuntu.com/questions/85221/turn-off-wine-debugging) and changes the wineuser home directory.

2. Go to the [DnaSP v6 website](http://www.ub.edu/dnasp/) and download it.

3. Uncompress the zip file. You must have an executable file named `DnaSP_v61203_x64.exe` or similar.

4. Run the `pegi3s/dnasp-v6` Docker image with: `docker run -it -v /path/to/dnasp:/path/to/dnasp pegi3s/dnasp-v6 bash`. Here you must replace `/path/to/dnasp` with the actual path that contains the DnaSP executable.

5. Once in the Docker container, change directory to `/path/to/dnasp` and run the following commands:

```bash
winecfg
winetricks -q dotnet45
winetricks vb6run
wine DnaSP_v61203_x64.exe
```

6. After completing the installations, leave the container and run the following command to update the image with the container: `docker commit <container_id> pegi3s/dnasp-v6`. Here you must replace `<container_id>` with the actual identifier of the recently executed container.
