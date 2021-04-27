FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential wget 
RUN wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2021-03-08.tar.gz -O /tmp/gmap-gsnap.tar && \
        tar -xvf /tmp/gmap-gsnap.tar && \
        rm /tmp/gmap-gsnap.tar -f
RUN     cd gmap-2021-03-08 && \
        ./configure && \
        make && \
        make install
