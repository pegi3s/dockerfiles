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
