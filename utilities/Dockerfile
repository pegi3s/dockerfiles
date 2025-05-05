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

FROM pegi3s/docker

RUN apt-get update && \
	apt-get install -y wget

RUN mkdir -p /opt/scripts && wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -O /opt/scripts/jq-linux64 

ARG utilities_version

ENV UTILITIES_VERSION=${utilities_version}

ADD scripts/help /usr/local/bin/help

ADD scripts /opt/scripts

RUN chmod 777 /opt/scripts/* && chmod u+x /usr/local/bin/help

ENV PATH="/opt/scripts:${PATH}"

ENV TERM=xterm-256color
