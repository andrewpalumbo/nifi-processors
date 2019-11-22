#!/usr/bin/env bash

.PHONY  conda-env@2.7 env java clean all docker-env deploy:

conda-env@2.7:
    ./scripts/install_conda_env.sh python2.7

env@2.7: conda-env@2.7

env@3.7:
    ./scripts/install_conda_env.sh

env: env@3.7

build: env

clean: mvn clean && \
       find ./RTL-SDR-ingestor/nifi-nifi-rf-nar/src/main/python -type f -name '*.pyc' -exec rm {}









