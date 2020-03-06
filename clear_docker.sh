#!/usr/bin/env sh

docker stop $(docker container ls -a -q)
docker rm $(docker container ls -a -q)
docker rmi $(docker image ls -a -q)
