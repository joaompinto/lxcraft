#!/usr/bin/env bash
git config  --global --add safe.directory /workspace
docker \
    run \
    -v $(pwd):/workspace \
    -v $HOME/.gitconfig:/root/.gitconfig \
    -v $HOME/.ssh:/root/.ssh \
    -it debian:12 \
    workspace/develop/setup.sh
