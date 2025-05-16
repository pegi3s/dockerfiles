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
	apt-get install -y build-essential && \
	apt-get install -y ca-certificates software-properties-common -y wget && \
        apt install apt-transport-https

RUN cd /opt && \ 
	wget https://ab.inf.uni-tuebingen.de/data/software/splitstree4/download/splitstree4_unix_4_14_8.sh && \
	chmod 777 /opt/splitstree4_unix_4_14_8.sh
RUN apt install -y default-jre
RUN { echo 'o' ; echo '1' ; echo '/opt/splitstree4' ; echo 'X,2,3' ; echo "n" ; echo '5' ; echo '1000' ; } | /opt/splitstree4_unix_4_14_8.sh

ENTRYPOINT [ "sh", "-c", "/opt/splitstree4/SplitsTree" ]

WORKDIR /data
