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

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-get install -y git ant wget

RUN apt-get update && \
	apt-get install -y openjdk-8-jdk && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN git clone https://github.com/ddarriba/jmodeltest2.git

RUN cd jmodeltest2 && ant jar

RUN cd /jmodeltest2/dist/exe/phyml && \
	wget https://github.com/713/project/raw/master/dependencies/jmodeltest-2.1.3/exe/phyml/PhyML_3.0_linux64 && \
	chmod 777 PhyML_3.0_linux64
