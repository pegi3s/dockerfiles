FROM ubuntu:19.04

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
