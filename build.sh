#!/bin/bash
#
# Usage ./build.sh repo/user [push]
#
IMAGE_PREFIX="${1:-app-simulator}"

for DIR in nodes/*;
do
  if [ -d $DIR ] ; then
    echo "Building ${IMAGE_PREFIX}/app-simulator:`basename $DIR`..."
    docker build --platform=linux/amd64  -t "${IMAGE_PREFIX}/app-simulator:`basename $DIR`" $DIR;
    if [ "$2" == "push" ]; then
        echo "Pushing ${IMAGE_PREFIX}/app-simulator:`basename $DIR` to registry ...."
        docker push "${IMAGE_PREFIX}/app-simulator:`basename $DIR`"
        # Add your commands here
    fi
  fi
done;

for DIR in loaders/*;
do
  if [ -d $DIR ] ; then
    echo "Building ${IMAGE_PREFIX}/app-simulator:`basename $DIR`..."
    docker build --platform=linux/amd64  -t "${IMAGE_PREFIX}/app-simulator:`basename $DIR`" $DIR;
    if [ "$2" == "push" ]; then
        echo "Pushing ${IMAGE_PREFIX}/app-simulator:`basename $DIR` to registry ...."
        docker push "${IMAGE_PREFIX}/app-simulator:`basename $DIR`"
        # Add your commands here
    fi
  fi
done;