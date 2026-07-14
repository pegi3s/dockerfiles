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

FROM ubuntu:24.04

ARG VERSION

RUN apt-get update && apt-get install -y wget unzip python3

RUN wget "https://sourceforge.net/projects/bowtie-bio/files/bowtie/${VERSION}/bowtie-${VERSION}-linux-x86_64.zip/download" -O /tmp/bowtie.zip && \
	unzip /tmp/bowtie.zip -d /opt && rm /tmp/bowtie.zip

ENV PATH="/opt/bowtie-${VERSION}-linux-x86_64/:${PATH}"

RUN apt-get remove -y wget unzip && apt-get clean
