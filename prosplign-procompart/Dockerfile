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
	&& apt-get install -y wget libkrb5-3 libsqlite3-0 libcurl3 ncbi-blast+=2.6.0-1 unzip

RUN wget static.sing-group.org/software/SEDA/dev_resources/pro-ncbi.tar.gz -O /tmp/pro-ncbi.tar.gz \
	&& mkdir /opt/pro-ncbi \
	&& tar zxvf /tmp/pro-ncbi.tar.gz -C /opt/pro-ncbi && rm /tmp/pro-ncbi.tar.gz

RUN ln -s -T /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libpcre.so.0 \
	&& ln -s /usr/lib/x86_64-linux-gnu/libdb-5.3.so /usr/lib/libdb-4.6.so

ENV PATH="/opt/pro-ncbi:${PATH}"

RUN mkdir /opt/java && cd /opt/java \
    && wget http://static.sing-group.org/software/dev-resources/java-installer-resources-linux-1.8.0_111.zip \
    && unzip java-installer-resources-linux-1.8.0_111.zip 'linux/64b/*' \
    && rm java-installer-resources-linux-1.8.0_111.zip

RUN wget https://maven.sing-group.org/repository/maven-releases/org/sing_group/prosplign-parser/1.0.0/prosplign-parser-1.0.0-jar-with-dependencies.jar -O /opt/pro-ncbi/prosplign-parser.jar

ENV PATH="/opt/java/linux/64b/jre1.8.0_111/bin/:${PATH}"

RUN apt-get remove -y wget

COPY --from=base_pegi3s_utilities /opt/scripts/fasta_replace_and_save_headers /opt/scripts/fasta_replace_and_save_headers

ADD scripts/prosplign-procompart-pipeline /opt/scripts/

RUN chmod u+x /opt/scripts/*

ENV PATH="/opt/scripts/:${PATH}"
