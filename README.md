## Setup

### Project

#### Replace project name

Since `module1` is tentatively specified for the module name, change the name as
it appears in the next configuration file.

- [pyproject.toml](pyproject.toml)
- [.flake8](.flake8)

### Docker

The `docker` directory is managed in the following structure.

```
docker
├── <image-1>
│   ├── image   Save the `Dockerfile` and any files the image needs here.
│   └── data   (Optional) Here is the file to mount in the Docker container.
├── <image-2>
│   ├── image 
│   └── data
```

#### [docker/python](docker/python)

This Docker image manages dependencies with `pip-tools`.
The dependencies are listed in the following file, so if you want to add a
dependency or upgrade dependencies, update the list and then upgrade
dependencies in the Docker container with `pip-compile` command.

- [docker/python/image/requirements.in](docker/python/image/requirements.in)
- [docker/python/image/dev-requirements.in](docker/python/image/dev-requirements.in)

Example:

```shell
$ cd docker/python/image
# Add dependencies.
$ vi requirements.in
# Update `requirements.txt`.
$ pip-compile requirements.in

# Add dev dependencies.
$ vi dev-requirements.in
# Update `dev-requirements.txt`.
$ pip-compile dev-requirements.in

# Upgrade all dependencies.
$ pip-compile --upgrade
# Upgrade <package>.
$ pip-compile --upgrade-package <package>
```

#### [docker-compose.yml](docker-compose.yml)

Edit [docker-compose.yml](docker-compose.yml).

#### Visual Studio Code Remote Development

Edit [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json) and
[.devcontainer/docker-compose.yml](.devcontainer/docker-compose.yml).
