#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y libdatetime-perl libxml-simple-perl libdigest-md5-perl git default-jre bioperl

RUN cpan Bio::Perl

RUN git clone https://github.com/tseemann/prokka.git /opt/prokka

RUN apt-get update && apt-get install -y wget libgomp1

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/ncbi-blast-2.13.0+-x64-linux.tar.gz -O /tmp/blast.tar.gz && \
	tar zxvf /tmp/blast.tar.gz -C /opt/ && rm /tmp/blast.tar.gz

# install tbl2asn manually since the one included with prokka is expired
RUN wget https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/2023-01-19/by_program/tbl2asn/linux64.tbl2asn.gz -O /tmp/linux64.tbl2asn.gz && \
    gunzip /tmp/linux64.tbl2asn.gz && chmod u+x /tmp/linux64.tbl2asn && mv /tmp/linux64.tbl2asn /opt/prokka/binaries/linux/tbl2asn
	
ENV PATH="/opt/ncbi-blast-2.13.0+/bin:/opt/prokka/bin:/opt/prokka/binaries/linux/:${PATH}"

RUN prokka --setupdb
