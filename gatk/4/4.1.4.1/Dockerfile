FROM ubuntu:19.04

WORKDIR /tmp

RUN apt-get update \
	&& apt-get install -y build-essential unzip wget \
	&& apt-get install -y ca-certificates software-properties-common

RUN apt-get update \
	&& apt-get install -y python-pip python2.7 python2.7-dev

RUN apt-get update \
	&& apt-get install -y openjdk-8-jre \
	&& rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/broadinstitute/gatk/releases/download/4.1.4.1/gatk-4.1.4.1.zip -O /tmp/gatk-4.1.4.1.zip\
	&& unzip /tmp/gatk-4.1.4.1.zip -d /opt/ \
	&& rm /tmp/gatk-4.1.4.1.zip -f \
	&& cd /opt/gatk-4.1.4.1 \
	&& ./gatk --list

ENV PATH="/opt/gatk-4.1.4.1/:${PATH}"
