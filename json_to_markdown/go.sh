#!/bin/sh
JSON_DIR=/home/fvbakel/git/PrimeTools/results/2021-08
docker build --pull --rm -f Dockerfile -t mypython:latest .
docker run --rm -it -v $PWD:/opt/app -v ${JSON_DIR}:/data  mypython:latest
