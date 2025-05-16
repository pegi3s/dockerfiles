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

RUN apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential perl wget

# RUN wget http://161.111.161.41/cgi-bin/translatorx_vLocal.pl -O /opt/translatorx_vLocal.pl
# Use a mirror since the public server (http://translatorx.co.uk) does not work sometimes
RUN wget http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/translatorx/translatorx_vLocal.pl -O /opt/translatorx_vLocal.pl && \
	chmod u+x /opt/translatorx_vLocal.pl

ENV PATH="/opt/:${PATH}"
