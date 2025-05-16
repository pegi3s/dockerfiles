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

FROM ubuntu:22.04

ARG VERSION

RUN apt-get update && apt-get install -y wget libgomp1 libnet-sftp-foreign-perl curl

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${VERSION}/ncbi-blast-${VERSION}+-x64-linux.tar.gz -O /tmp/blast.tar.gz && \
	tar zxvf /tmp/blast.tar.gz -C /opt/ && rm /tmp/blast.tar.gz

ENV PATH="/opt/ncbi-blast-${VERSION}+/bin:${PATH}"
