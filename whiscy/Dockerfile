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

FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install python3 python3-numpy python3-nose2 python3-biopython gcc git-all wget

RUN wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz -O /tmp/muscle.tar.gz && \
	tar -xzvf /tmp/muscle.tar.gz -C /opt/ && \
	rm /tmp/muscle.tar.gz -f

# FreeSASA dependencies
RUN apt-get install -y libxml2-dev libjson-c-dev

RUN wget https://freesasa.github.io/freesasa-2.0.3.tar.gz -O /tmp/freesasa.tar.gz && \
	tar -xzvf /tmp/freesasa.tar.gz -C /opt/ && \
	rm /tmp/freesasa.tar.gz -f && \
	cd /opt/freesasa-2.0.3 && \
	./configure && make && make install

RUN cd /opt && \
  git clone https://github.com/haddocking/whiscy.git

ENV WHISCY_PATH=/opt/whiscy
ENV PYTHONPATH=$PYTHONPATH:${WHISCY_PATH}
ENV WHISCY_BIN=${WHISCY_PATH}/whiscy.py
ENV PATH=$PATH:${WHISCY_PATH}

RUN cd /opt/whiscy/bin/protdist && chmod u+x -R ../protdist/ && ./compile.sh

RUN sed -i 's%/Users/bjimenez/bin/muscle/muscle3.8.31_i86darwin64%/opt/muscle3.8.31_i86linux64%g' /opt/whiscy/etc/local.json

WORKDIR /data
