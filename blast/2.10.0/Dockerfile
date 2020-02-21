FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.0/ncbi-blast-2.10.0+-x64-linux.tar.gz -O /tmp/blast.tar.gz && \
	tar zxvf /tmp/blast.tar.gz -C /opt/ && rm /tmp/blast.tar.gz

ENV PATH="/opt/ncbi-blast-2.10.0+/bin:${PATH}"
