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

LABEL coral.version="1.4.1" \
      coral.web="https://www.cs.helsinki.fi/u/lmsalmel/coral/"

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y wget build-essential

RUN  wget https://www.cs.helsinki.fi/u/lmsalmel/coral/coral-1.4.1.tar.gz -O /tmp/coral.tar.gz && \
	tar -xvzf /tmp/coral.tar.gz -C /opt/ && \
	rm /tmp/coral.tar.gz && \
	cd /opt/coral-1.4.1 && \
	make

ENV PATH="/opt/coral-1.4.1/:${PATH}"

RUN apt-get autoremove -y wget

ENTRYPOINT ["coral"]
CMD ["-h"]
