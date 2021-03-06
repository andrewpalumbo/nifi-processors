#!/usr/bin/env bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

set -ex

export SET_PYTHON_VERSION=false
export PYTHON_VERSION=3.7  #default version to 3.7

if [[ "$1" -gt "-1" ]]
  then SET_PYTHON_VERSION=TRUE
fi

conda create cusignal-nifi
conda activate cusignal-nifi
if [[set_PYTHON_VERSION]];
 then  conda install --python@1 -f cusignal_conda_env.yml
else
   conda install  --python@1 -f cusignal_conda_env.yml
fi


