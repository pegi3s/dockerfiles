FROM ubuntu:16.04

RUN apt-get -qq update && apt-get -y upgrade && \
	apt install -y wget unzip make g++

RUN wget https://github.com/aquaskyline/SOAPdenovo2/archive/master.zip -O /opt/master.zip && \
	cd /opt && unzip master.zip && \
	rm master.zip && \
	cd /opt/SOAPdenovo2-master/ && \
	make

ENV PATH="/opt/SOAPdenovo2-master/:${PATH}"





