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

FROM ubuntu:18.04

LABEL edena.version="V3.131028" \
      edena.web="http://www.genomic.ch/edena.php"

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y wget build-essential

RUN wget http://www.genomic.ch/edena/EdenaV3.131028.tar.gz -O /tmp/edena.tar.gz && \
	tar -xvzf /tmp/edena.tar.gz -C /opt && \
	rm /tmp/edena.tar.gz && \
	cd /opt/EdenaV3.131028 && \
	make

ENV PATH="/opt/EdenaV3.131028/bin/:${PATH}"

RUN apt-get autoremove -y wget build-essential	

ENTRYPOINT ["edena"]
CMD ["-h"]
