#!/usr/bin/env bash -l

# CHECK IF DOCKER IS INSTALLED | IF NOT, INSTALL IT
if command -v docker >/dev/null 2>&1 ; then
    echo "Docker found"
    echo "version: $(docker -v)"
else
    echo "Docker not found. Installing..."
    sh ./get-docker.sh
fi

# CHECK, CREATE AND ACTIVATE CONDA ENVIRONMENT
conda activate xpore || conda create -y --name xpore python && conda activate xpore

# MAKE CYCLEDELIC DIRECTORY IF ONE DOESN'T EXIST
sudo mkdir -p  ~/cycledelic/xpore/docker/volumes/grafana/grafana-provisioning \
    ~/cycledelic/xpore/docker/volumes/postgresql/pgdata \
    ~/cycledelic/xpore/docker/volumes/portainer/data

