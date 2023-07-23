#!/bin/bash
set -eu
apt update
apt -y install curl bzip2 git
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -C /usr/local -xj bin/micromamba
export MAMBA_ROOT_PREFIX=~/micromamba
mkdir -p $MAMBA_ROOT_PREFIX
micromamba shell init -s bash -p $MAMBA_ROOT_PREFIX
source ~/.bashrc
micromamba config append channels conda-forge
micromamba -n base install -y python=3.11
cd /workspace
echo micromamba activate base >> ~/.bashrc
bash
