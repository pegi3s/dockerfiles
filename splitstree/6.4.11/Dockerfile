#
#   Copyright 2018-2026 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN apt-get update -y && \
	apt-get install -y wget default-jre

RUN cd /opt && \ 
	wget https://software-ab.cs.uni-tuebingen.de/download/splitstree6/SplitsTree_unix_6_4_11.sh && \
	chmod 777 /opt/SplitsTree_unix_6_4_11.sh

RUN bash -c "{ echo 'o' ; for i in {1..29}; do echo $i; done; echo '1' ; echo '/opt/splitstree6' ; echo 'X,2' ; echo 'y' ; echo '/usr/local/bin' ; echo '5' ; echo '512'; } | /opt/SplitsTree_unix_6_4_11.sh -c"

RUN rm /opt/SplitsTree_unix_6_4_11.sh

ENTRYPOINT [ "SplitsTree" ]
