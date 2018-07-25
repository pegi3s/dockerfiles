FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential unzip wget

RUN wget http://www.danielwilson.me.uk/omegaMap/omegaMap.zip -O /tmp/omegaMap.zip && \
	unzip /tmp/omegaMap.zip -d /opt/ && \
	rm /tmp/omegaMap.zip -f && \
	cd /opt/omegaMap && \
	make

COPY additional-utils /opt/omegaMap/additional-utils

ENV PATH="/opt/omegaMap/:${PATH}"
ENV PATH="/opt/omegaMap/additional-utils:${PATH}"