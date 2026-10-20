# Running Docker commands inside Docker containers on macOS

On macOS, Docker Desktop runs the Docker daemon inside a virtual machine. To run Docker commands from inside a container, the container must access the Docker daemon exposed by Docker Desktop. This guide explains the required configuration and uses the graphical interface of [SEDA](https://www.sing-group.org/seda/) as an example.

## 1. How it works

Docker Desktop exposes its Docker daemon through the `/var/run/docker.sock` symbolic link. To make that daemon available to a container, mount this symbolic link and tell the Docker client inside the container where to connect:

```shell
-v /var/run/docker.sock:/var/run/docker.sock
-e DOCKER_HOST=unix:///var/run/docker.sock
```

Use `/var/run/docker.sock`, not the socket path of the active Docker context.

## 2. What must be checked

Before running the container, check the following:

- **Docker Desktop is running.**
- **The active Docker context is `desktop-linux`.** Run:

  ```shell
  docker context ls
  ```

  The active context is marked with `*`. If it is not `desktop-linux`, switch to it with `docker context use desktop-linux`.

- **`/var/run/docker.sock` exists and is the symbolic link used by Docker Desktop.** Run:

  ```shell
  ls -l /var/run/docker.sock
  ```

  The output should look like:

  ```
  lrwxr-xr-x  1 root  daemon  37 24 sept. 17:44 /var/run/docker.sock -> /Users/<user>/.docker/run/docker.sock
  ```

- **The server platform is known.** Run:

  ```shell
  docker info --format 'Server={{.OSType}}/{{.Architecture}}'
  ```

  On Apple Silicon this prints `Server=linux/aarch64`. Since the images from this project are built for `linux/amd64`, the `--platform linux/amd64` option is required.

- **The Docker API versions are compatible.** Run:

  ```shell
  docker version --format 'Client API: {{.Client.APIVersion}} / Server API: {{.Server.APIVersion}}'
  ```

  The server API version is the maximum version supported by the Docker Desktop daemon. If the Docker client inside the container is newer, see section 4.

## 3. Minimal example

Run a container with access to the Docker daemon:

```shell
docker run --rm -ti \
  --platform linux/amd64 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e DOCKER_HOST=unix:///var/run/docker.sock \
  pegi3s/docker bash
```

Then, inside the container, run:

```shell
docker info
docker images
```

The output should be the same as when running these commands on the host, which confirms that Docker is working inside the container.

## 4. Docker API compatibility

The Docker client bundled in an image may be newer than the Docker daemon running in Docker Desktop. When this happens, Docker commands fail because the client requests an API version that the daemon does not support.

In that case, set `DOCKER_API_VERSION` to a version supported by the daemon. For example, if the client uses API 1.52 and the daemon supports up to 1.43, add:

```shell
-e DOCKER_API_VERSION=1.43
```

The value is environment-dependent: use the server API version reported in section 2, and update it if Docker Desktop is upgraded. If the client and daemon versions are compatible, this variable can be omitted.

## 5. Example: SEDA with Docker support

Some graphical applications, such as SEDA, need to run Docker commands themselves, for example to launch sibling containers that execute their tools. The complete command to run the SEDA graphical interface with access to Docker Desktop is:

```shell
docker run --rm -ti \
  --platform linux/amd64 \
  -e USERID=$(id -u) \
  -e USER=$(whoami) \
  -e DISPLAY=host.docker.internal:0 \
  -e DOCKER_HOST=unix:///var/run/docker.sock \
  -e DOCKER_API_VERSION=1.43 \
  -v "$HOME/Documents/Docker:/data" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  pegi3s/seda:1.7.5-docker29.0.1
```

This command includes the options required to run a graphical application (`--platform`, `USERID`, `USER`, `DISPLAY` and the `/data` volume) together with the Docker-in-Docker options:

- `-v /var/run/docker.sock:/var/run/docker.sock` exposes the Docker Desktop daemon to the container.
- `-e DOCKER_HOST=unix:///var/run/docker.sock` tells the Docker client inside the container where to connect.
- `-e DOCKER_API_VERSION=1.43` sets the API version used by the client, as explained in section 4.

Before running the command, XQuartz must be running and `/opt/X11/bin/xhost +localhost` must have been executed since the last time XQuartz was started. The tutorial on running GUI applications from our Docker images on macOS describes how to install and configure XQuartz.

## 6. Troubleshooting

- **`Cannot connect to the Docker daemon`**: check that Docker Desktop is running, that the active context is `desktop-linux`, and that the container mounts `/var/run/docker.sock` and sets `DOCKER_HOST=unix:///var/run/docker.sock`.
- **`client version ... is too new. Maximum supported API version is ...`**: set `DOCKER_API_VERSION` to the maximum version reported for the server.
- **`operation not supported` when starting the container**: use `/var/run/docker.sock` instead of the socket path of the active Docker context.
- **The graphical application does not open**: check that XQuartz is running and that `/opt/X11/bin/xhost +localhost` has been executed since the last XQuartz restart, and that the command includes `-e DISPLAY=host.docker.internal:0`.

---

**Compatibility note:** This procedure was tested on a MacBook Pro with an Apple M4 processor running macOS 26.2, using Docker Desktop and the `pegi3s/seda:1.7.5-docker29.0.1` image, with both the graphical interface and Docker-in-Docker working successfully. The required `DOCKER_API_VERSION` depends on the Docker Desktop version and may differ on other systems.
