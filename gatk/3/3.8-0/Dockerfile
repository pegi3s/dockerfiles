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

FROM ubuntu:19.04

RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

WORKDIR /tmp

RUN apt-get update \
	&& apt-get install -y build-essential gzip wget curl \
	&& apt-get install -y ca-certificates software-properties-common

RUN apt-get update \
	&& apt-get install -y openjdk-8-jre \
	&& rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

ENV gatk_version 3.8-0
RUN curl -L https://github.com/Miachol/gatk_releases/raw/master/gatk${gatk_version}.tar.gz -o gatk.tar.gz \
	&& tar -xzvf gatk.tar.gz \
	&& mv gatk${gatk_version}/GenomeAnalysisTK.jar /opt \
	&& chmod 644 /opt/GenomeAnalysisTK.jar \
	&& rm -rf *

ENV picard_version 2.18.11

RUN wget https://github.com/broadinstitute/picard/releases/download/${picard_version}/picard.jar -O /opt/picard.jar \
	&& chmod 644 /opt/picard.jar
