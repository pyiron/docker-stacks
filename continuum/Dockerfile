ARG ROOT_CONTAINER=pyiron/md:latest
ARG BASE_CONTAINER=$ROOT_CONTAINER
FROM $BASE_CONTAINER

MAINTAINER Jan Janssen <janssen@mpie.de>, Muhammad Hassani <hassani@mpie.de>


USER root
COPY apt.txt /tmp/
# installing build-essential
RUN apt-get update -y && \
    xargs -a /tmp/apt.txt apt-get install -y && \
    apt-get clean && \
    rm /tmp/apt.txt

USER $DOCKER_UID
WORKDIR $HOME
ARG PYTHON_VERSION=default

COPY . ${HOME}/
RUN conda env update -n base -f ${HOME}/environment.yml --prune && \
    conda clean --all -f -y && \
    conda list

USER root
RUN rm ${HOME}/*.ipynb &&\
    chmod +x ${HOME}/include_notebooks.sh && \
    /bin/bash ${HOME}/include_notebooks.sh && \
    fix-permissions /home/$DOCKER_USER && \
    fix-permissions $CONDA_DIRs

# Switch back to pyiron to avoid accidental container runs as root
USER $DOCKER_UID

WORKDIR $HOME
