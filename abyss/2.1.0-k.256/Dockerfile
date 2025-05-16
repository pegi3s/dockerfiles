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

RUN apt-get -qq update && \
	apt-get install -y --no-install-recommends wget \
	bsdmainutils libgomp1 make openmpi-bin ssh \
	automake g++ libboost-dev libopenmpi-dev libsparsehash-dev

RUN wget --no-check-certificate https://github.com/bcgsc/abyss/releases/download/2.1.0/abyss-2.1.0.tar.gz -O /tmp/abyss.tar.gz && \
	tar zxvf /tmp/abyss.tar.gz -C /opt/ && rm /tmp/abyss.tar.gz && \
	cd /opt/abyss-2.1.0 && \
	./autogen.sh && \
	mkdir build && cd build && \
	../configure --with-mpi=/usr/lib/openmpi --enable-maxk=256 && \
	make install-strip && \
	rm -rf /tmp/abyss

RUN apt-get autoremove -y binutils automake g++ libboost-dev libopenmpi-dev libsparsehash-dev wget
