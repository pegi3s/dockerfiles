FROM pegi3s/utilities:0.13.0 as base_pegi3s_utilities

FROM ubuntu:18.04

RUN apt-get update \
	&& apt-get install -y wget libkrb5-3 libsqlite3-0 libcurl3 ncbi-blast+=2.6.0-1 build-essential bzip2 libz-dev libbz2-dev liblzma-dev

RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.2/bedtools-2.29.2.tar.gz -O /tmp/bedtools.tar.gz && \
	tar zxvf /tmp/bedtools.tar.gz -C /opt/ && rm /tmp/bedtools.tar.gz && \
	cd /opt/bedtools2 && \
	make

ENV PATH="/opt/bedtools2/bin/:${PATH}"

RUN wget static.sing-group.org/software/SEDA/dev_resources/splign-compart.tar.gz -O /tmp/splign-compart.tar.gz \
	&& mkdir /opt/splign-compart \
	&& tar zxvf /tmp/splign-compart.tar.gz -C /opt/splign-compart && rm /tmp/splign-compart.tar.gz

RUN ln -s -T /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libpcre.so.0

ENV PATH="/opt/splign-compart:${PATH}"

RUN apt-get remove -y wget build-essential

COPY --from=base_pegi3s_utilities /opt/scripts/fasta_remove_line_breaks /opt/scripts/fasta_remove_line_breaks
COPY --from=base_pegi3s_utilities /opt/scripts/fasta_reverse_complement  /opt/scripts/fasta_reverse_complement

ADD scripts/splign-compart-pipeline /opt/scripts/

RUN chmod u+x /opt/scripts/*

ENV PATH="/opt/scripts/:${PATH}"
