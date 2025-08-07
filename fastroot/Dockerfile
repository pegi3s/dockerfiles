#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
#   Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

FROM python:3.9

RUN pip install --upgrade pip && \
    pip install --no-cache-dir FastRoot==1.5 treeswift==1.1.14 cvxopt==1.2.5 numpy==1.26.0

RUN apt-get update -y && \
    apt-get install dos2unix && \
    dos2unix /usr/local/bin/FastRoot.py && \
    apt-get remove -y dos2unix

ENTRYPOINT ["FastRoot.py"]
