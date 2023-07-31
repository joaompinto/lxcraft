#!/usr/bin/env bash
import os

base_dir = os.environ.get("USERPROFILE", os.getcwd())

cmd = (
    "docker run"
    f" -v {base_dir}:{base_dir}"
    " -v $HOME/.gitconfig:/root/.gitconfig -v $HOME/.ssh:/root/.ssh"
    " -it debian:12 $(pwd)/develop/setup.sh $(pwd)"
)
print(cmd)
os.system(cmd)
