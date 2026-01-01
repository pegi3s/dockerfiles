#
#   Copyright 2018-2026 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

FROM ubuntu:20.04

ARG VERSION=2.1.0

RUN apt-get update && apt-get upgrade -y && apt-get install -y unzip wget python2.7 && \
    ln -s /usr/bin/python2.7 /usr/bin/python

RUN DOWNLOAD_VERSION=$(echo $VERSION | sed 's/\.//g') && \
    wget https://cloud.biohpc.swmed.edu/index.php/s/hisat2-${DOWNLOAD_VERSION}-Linux_x86_64/download -O /tmp/hisat.zip && \
    unzip /tmp/hisat.zip -d /opt/ && \
    rm /tmp/hisat.zip

ENV PATH="/opt/hisat2-${VERSION}/:/opt/hisat2-${VERSION}/scripts:${PATH}"
