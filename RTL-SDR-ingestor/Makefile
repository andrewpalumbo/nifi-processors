#!/usr/bin/env bash

.PHONY  conda-env@2.7 env java clean all docker-env deploy clean clean-env conda-env@2.7 env@3.7 env@2.7 all@2.7:

    ./scripts/install_conda_env.sh python2.7

env@2.7: conda-env@2.7

env@3.7:
    ./scripts/install_conda_env.sh

env: env@3.7

java: clean-env env && \
      package

clean: mvn clean && \
       find ./RTL-SDR-ingestor/nifi-nifi-rf-nar/src/main/python -type f -name '*.pyc' -exec rm {}

all@2.7: clean clean-env@2.7 env@2.7 package

all: clean clean-env env package

clean-env: conda clean --all && \

clean-env2.7: conda clean-env --all  && \

clean-all: clean-env clean

package: mvn clean clean-env release

install: all

deploy:














