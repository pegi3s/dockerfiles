FROM ubuntu:19.04

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y python3-pip python3-dev build-essential wget bzip2 libz-dev libbz2-dev liblzma-dev && \
	ln -s /usr/bin/python3 /usr/bin/python

RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools-2.30.0.tar.gz -O /tmp/bedtools.tar.gz && \
	tar zxvf /tmp/bedtools.tar.gz -C /opt/ && rm /tmp/bedtools.tar.gz && \
	cd /opt/bedtools2 && \
	make

ENV PATH="/opt/bedtools2/bin/:${PATH}"
