#!/usr/bin/env bash

source $(dirname $BASH_SOURCE[0])/variables.sh

# TODO: check to see if the docker image exists
docker run -it --rm --name $IMAGE_NAME $CONTAINER_NAME
