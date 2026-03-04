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

RUN apt-get update \
	&& apt-get -y upgrade \
	&& apt-get install -y wget make gcc

RUN wget https://dialign.gobics.de/download/dialign_package.tgz -O 	/tmp/dialign_package.tgz \
	&& tar zxvf /tmp/dialign_package.tgz -C /opt/ && rm 	/tmp/dialign_package.tgz

# Create an environment variable pointing to the directory (setenv Step)
ENV DIALIGN2_DIR=/opt/dialign_package/dialign2_dir/

WORKDIR /opt/dialign_package/src/

RUN make && rm -f *.o