#
#   Copyright 2018-2021 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common

# Install Python
RUN apt-get install -y python-pip python2.7 python2.7-dev

# Install PyPy
RUN add-apt-repository ppa:pypy/ppa && \
	apt-get update && \
	apt-get install -y pypy pypy-dev

RUN wget https://github.com/OpenGene/AfterQC/archive/v0.9.7.zip -O /tmp/AfterQC-0.9.7.zip && \
	unzip /tmp/AfterQC-0.9.7.zip -d /opt/ && \
	rm /tmp/AfterQC-0.9.7.zip -f && \
	cd /opt/AfterQC-0.9.7 && \
	make

ENV PATH="/opt/AfterQC-0.9.7/:${PATH}"
