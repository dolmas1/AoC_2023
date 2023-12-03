#!/bin/bash

IMAGE=majikthise/aoc-2023:3

docker image inspect $IMAGE >/dev/null 2>&1
if [ $? -ne 0 ]
then
    echo "One time setup: building docker image..."
    docker build docker -t $IMAGE
fi

docker run \
    --rm \
    -it \
    -v "$(pwd)":/code \
    $IMAGE \
    /entrypoint.sh $@