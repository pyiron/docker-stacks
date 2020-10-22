ARG ROOT_CONTAINER=pyiron/atomistic:latest
ARG BASE_CONTAINER=$ROOT_CONTAINER
FROM $BASE_CONTAINER

MAINTAINER Jan Janssen <janssen@mpie.de>, Muhammad Hassani <hassani@mpie.de>

USER $DOCKER_UID
WORKDIR $HOME
ARG PYTHON_VERSION=default

COPY . ${HOME}/
#RUN conda install --quiet -y -c conda-forge lammps &&\
RUN conda env update -n base -f ${HOME}/environment.yml && \
    conda clean --all -f -y && \
    npm cache clean --force

USER root
RUN fix-permissions /home/$DOCKER_USER &&\
    fix-permissions $CONDA_DIR && \
    chmod +x ${HOME}/include_notebooks.sh && \
    /bin/bash include_notebooks.sh &&\
    fix-permissions /home/$DOCKER_USER && \
    chown -R ${DOCKER_USER}:${DOCKER_GID} ${HOME}/*.ipynb

# Switch back to pyiron to avoid accidental container runs as root
USER $DOCKER_UID

WORKDIR $HOME