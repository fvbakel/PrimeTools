#!/bin/sh
DATA_DIR=/home/fvbakel/Documenten/primes
docker build --pull --rm -f Dockerfile -t mypython:latest .
docker run --rm -it -p 8888:8888 -v $PWD:/opt/app -v ${DATA_DIR}:/data  mypython:latest
