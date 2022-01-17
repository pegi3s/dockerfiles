#
#   Copyright 2018-2022 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
	apt-get install -y unzip wget ca-certificates software-properties-common openjdk-11-jdk && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/

RUN wget https://github.com/rambaut/figtree/releases/download/v1.4.4/FigTree.v1.4.4.zip -O /tmp/figtree.zip && \
	unzip /tmp/figtree.zip -d /opt/ && rm /tmp/figtree.zip && \
	mv "/opt/FigTree v1.4.4" /opt/figtree

RUN echo '#!/bin/bash \n\
java -jar /opt/figtree/lib/figtree.jar $*' > /opt/figtree/run_figtree && \
    chmod u+x /opt/figtree/run_figtree

ENV PATH="/opt/figtree/:${PATH}"

ENTRYPOINT ["run_figtree"]
