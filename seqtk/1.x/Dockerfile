#
#   Copyright 2018-2023 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN apt-get update && apt-get install -y wget build-essential libz-dev

RUN wget "https://github.com/lh3/seqtk/archive/refs/tags/v${VERSION}.tar.gz" -O /tmp/seqtk.tar.gz && \
	tar zxvf /tmp/seqtk.tar.gz -C /opt && rm /tmp/seqtk.tar.gz && mv /opt/* /opt/seqtk && \
	cd /opt/seqtk/ && make
	
ENV PATH="/opt/seqtk/:${PATH}"

RUN apt-get remove -y wget build-essential libz-dev

ENTRYPOINT ["seqtk"]
