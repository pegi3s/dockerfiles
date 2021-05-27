#
#   Copyright 2018-2021 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
#   Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

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

RUN wget https://github.com/shenwei356/seqkit/releases/download/v0.12.1/seqkit_linux_amd64.tar.gz -O /tmp/seqkit.tar.gz && \
	tar zxvf /tmp/seqkit.tar.gz -C /usr/bin/ && rm /tmp/seqkit.tar.gz

RUN apt-get remove -y wget build-essential

COPY --from=base_pegi3s_utilities /opt/scripts/fasta_remove_line_breaks /opt/scripts/fasta_remove_line_breaks
COPY --from=base_pegi3s_utilities /opt/scripts/fasta_reverse_complement /opt/scripts/fasta_reverse_complement

ADD scripts/splign-compart-pipeline /opt/scripts/

RUN chmod u+x /opt/scripts/*

ENV PATH="/opt/scripts/:${PATH}"
