FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y mrbayes

WORKDIR /data/

ENV PATH="/opt/mrbayes.3.2.6-ubuntu64/bin/:${PATH}"
