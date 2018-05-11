FROM ubuntu:18.04

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y python3-pip python3-dev build-essential wget bzip2 libz-dev && \
	ln -s /usr/bin/python3 /usr/bin/python
	
RUN pip3 install regex

RUN  wget http://cab.spbu.ru/files/release3.11.1/SPAdes-3.11.1-Linux.tar.gz -O /tmp/spades.tar.gz && \
     tar -xvzf /tmp/spades.tar.gz -C /opt/ && \
     rm /tmp/spades.tar.gz

ENV PATH="/opt/SPAdes-3.11.1-Linux/bin/:${PATH}"
