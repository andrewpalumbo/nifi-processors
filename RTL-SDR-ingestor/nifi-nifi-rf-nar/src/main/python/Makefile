#!/usr/bin/env bash

.PHONY  env@2.7 env java-build python-build all clean clean-env clean-env@2.7 \
 docker-env deploy clean clean-env conda-env@2.7 env@3.7 env@2.7 all@2.7:


all@2.7:

clean@2.7:

clean-env@2.7: conda deactivate -n=cusignal-nifi

env@2.7: conda-env create --file cusignal_conda_dev-env.yml python=2.7 \
    conda activate cusignal-nifi

env: conda-env create --file cusignal_conda_dev-env.yml python=2.7 \
    conda activate cusignal-nifi
