#!/bin/bash
set -eu

export PIP_ROOT_USER_ACTION=ignore

apt update
apt -y install curl bzip2 git
MICROMAMBA_BIN=/usr/local/bin/micromamba

curl -Lo $MICROMAMBA_BIN \
    https://github.com/mamba-org/micromamba-releases/releases/download/1.4.9-0/micromamba-linux-64
chmod 755 $MICROMAMBA_BIN
export MAMBA_ROOT_PREFIX=~/micromamba
mkdir -p $MAMBA_ROOT_PREFIX
micromamba shell init -s bash -p $MAMBA_ROOT_PREFIX
source ~/.bashrc
micromamba config append channels conda-forge
micromamba -n base install -y python=3.11 just
echo micromamba activate base >> ~/.bashrc
[[ $# -gt 0 ]] && cd $1 && bash
