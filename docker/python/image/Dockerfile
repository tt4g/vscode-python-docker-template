ARG PYTHON_VERSION=3.10.6
# https://hub.docker.com/_/python
FROM python:${PYTHON_VERSION}-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # Development tools.
    git sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG PROJECT_DIR=/usr/src/app
WORKDIR ${PROJECT_DIR}
ADD dev-requirements.in dev-requirements.txt requirements.in requirements.txt ${PROJECT_DIR}

RUN python -m pip install --upgrade --no-cache-dir pip \
    # Install dependency management tool `pip-tools`.
    && python -m pip install --no-cache-dir pip-tools \
    && pip-sync --pip-args "--no-cache-dir" requirements.txt dev-requirements.txt

ARG PROJECT_UID=1000
ARG PROJECT_GID=1000
ARG PROJECT_USERNAME=project_user
ARG PROJECT_GROUPNAME=project_user
ARG PROJECT_PASSWORD=project_user
# Add user and group.
RUN groupadd -g ${PROJECT_GID} ${PROJECT_GROUPNAME} \
    && useradd -m -s /bin/bash -u ${PROJECT_UID} -g ${PROJECT_GID} ${PROJECT_USERNAME} \
    && echo "${PROJECT_USERNAME}:${PROJECT_PASSWORD}" | chpasswd \
    && echo "${PROJECT_USERNAME}   ALL=(ALL:ALL) ALL" > "/etc/sudoers.d/${PROJECT_GROUPNAME}" \
    && chmod 0440 "/etc/sudoers.d/${PROJECT_GROUPNAME}"
USER ${PROJECT_UID}:${PROJECT_GID}
