#!/bin/bash
set -eu

export PIP_ROOT_USER_ACTION=ignore

apt update
apt -y install curl bzip2 git python3 python3-pip python3-venv
python3 -m venv /usr/local/bin/python3.11
source /usr/local/bin/python3.11/bin/activate
pip install --upgrade pip setuptools wheel
pip install --upgrade invoke
echo "source /usr/local/bin/python3.11/bin/activate" >> ~/.bashrc

[[ $# -gt 0 ]] && cd $1 && bash
