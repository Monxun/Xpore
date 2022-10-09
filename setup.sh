#!/bin/bash

# SET TO RUN CONDA
set -euo pipefail

# CHECK IF MINICONDA IS INSTALLED | IF NOT, INSTALL IT
if command -v conda >/dev/null 2>&1 ; then
    echo "Miniconda found"
    echo "version: $(conda -v)"
else
    echo "Miniconda(conda) not found. Installing..."
    source ./cli/ansible/scripts/linux/install-miniconda.sh
fi

# CHECK, CREATE AND ACTIVATE CONDA ENVIRONMENT
conda activate xpore || conda create -y --name xpore python && conda activate xpore

# COPY USER SETTINGS CONFIG TO ANSIBLE TMP DIRECTORY
yes | cp -rf user_settings.yml ./scr/cli/ansible/vars/user_settings.yml

# INSTALL / RUN XPORE
cd cli

# CHECK IF XPORE IS INSTALLED | IF NOT, INSTALL IT
if command -v xpore >/dev/null 2>&1 ; then
    echo "xpore found"
    echo "version: $(xpore -v)"
else
    echo "Xpore not found. Installing..."
    pip install --editable .
fi

xpore init