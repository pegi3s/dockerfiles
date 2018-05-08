FROM ubuntu:18.04

RUN apt-get update \
	&& apt-get install -y wget make g++ libargtable2-dev

RUN wget http://www.clustal.org/omega/clustal-omega-1.2.4.tar.gz -O /tmp/clustalomega.tar.gz \
	&& tar zxvf /tmp/clustalomega.tar.gz -C /opt/ && rm /tmp/clustalomega.tar.gz \
	&& cd /opt/clustal-omega-1.2.4/ \
	&& ./configure && make && make install

ENTRYPOINT ["clustalo"]