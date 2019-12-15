#!/usr/bin/env bash

.PHONY  env@2.7 env java-build python-build all clean clean-env clean-env@2.7 \
 docker-env deploy clean clean-env conda-env@2.7 env@3.7 env@2.7 all@2.7:

    ./scripts/install_conda_env.sh python2.7

env@2.7: conda-env@2.7

env@3.7:
    ./scripts/install_conda_env.sh

env: env@3.7

java-build: clean-env env && \
      package

java-clean: 
    cd RTL-SDR-ingestor && ./mvn clean

python-build:
    clean-env env && \
    conda - && \
    conda   && \

python install:


python-clean:
    find ./RTL-SDR-ingestor/nifi-nifi-rf-nar/src/main/python -type f -name '*.pyc' -exec rm {}

clean:
    ./RTL-SDR-ingestor/mvn clean && \
    find ./RTL-SDR-ingestor/nifi-nifi-rf-nar/src/main/python -type f -name '*.pyc' -exec rm {}

all@2.7: clean clean-env@2.7 env@2.7 package

all: clean clean-env env package

clean-env: conda clean --all && \

clean-env2.7: conda clean-env --all  && \

clean-all: clean-env clean

package:
  cd RTL-SDR-ingestor && \
  python-clean &&
  python-build
  python-install

install: all

deploy: clean 














