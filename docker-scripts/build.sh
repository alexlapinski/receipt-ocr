#!/usr/bin/env bash

source $(dirname $BASH_SOURCE[0])/variables.sh

docker build -t $CONTAINER_NAME .
