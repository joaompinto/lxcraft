#!/usr/bin/env bash
set -eu

git config --global --add safe.directory $(pwd)

docker \
    run \
    -v $(pwd):$(pwd) \
    -v $HOME/.gitconfig:/root/.gitconfig \
    -v $HOME/.ssh:/root/.ssh \
    -it debian:12 \
    $(pwd)/develop/setup.sh $(pwd)
