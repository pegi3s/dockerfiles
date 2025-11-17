# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image provides a Docker installation and it was created to be user to create other images that need to invoke docker commands. This is done by exposing the Docker socket to the container (i.e. bind-mounting it with the `-v` flag) and starting it with `docker run -v /var/run/docker.sock:/var/run/docker.sock [...]`
