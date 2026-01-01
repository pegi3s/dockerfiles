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

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common

RUN apt-get update && \
	apt-get install -y openjdk-8-jdk && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update && apt-get install -y git maven

RUN wget https://github.com/sing-group/ALTER/archive/v1.3.4.tar.gz -O /tmp/alter.tar.gz && \
	tar zxvf /tmp/alter.tar.gz -C /opt/ && rm /tmp/alter.tar.gz && \
	mv /opt/ALTER-* /opt/ALTER && \
	cd /opt/ALTER && mvn package

RUN echo '#!/bin/bash \n\
java -jar /opt/ALTER/alter-lib/target/ALTER-1.3.4-jar-with-dependencies.jar $*' > /opt/ALTER/alter && chmod u+x /opt/ALTER/alter

ENV PATH="/opt/ALTER/:${PATH}"

ENTRYPOINT ["alter"]
