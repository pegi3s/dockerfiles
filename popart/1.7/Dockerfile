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

FROM ubuntu:14.04

RUN apt-get update && apt-get install -y software-properties-common && \
	apt-get install -y libqt4-dev && \
	apt-get install -y libmarble-dev && \
	apt-get install -y lp-solve && \
	apt-get install -y liblpsolve55-dev && \
        apt-get install -y uuid-runtime && \
	apt-get install -y dbus

RUN apt-get update && apt-get install -y build-essential unzip wget

RUN wget http://popart.otago.ac.nz/software/popart-1.7.tar.bz2 -O /tmp/popart-1.7.tar.bz2 && \
	tar xvf /tmp/popart-1.7.tar.bz2 -C /opt/ && rm /tmp/popart-1.7.tar.bz2 && \
	sed -i '0,/\-llpsolve55 \-lmarblewidget/{s/\-llpsolve55 \-lmarblewidget/\-L\/usr\/lib\/lp_solve\/ \-llpsolve55 \-lmarblewidget \-ldl\n  QMAKE_RPATHDIR \+\= \/usr\/lib\/lp_solve\//}' /opt/popart-1.7/src/popart.pro && \
	cd /opt/popart-1.7/src && \
	qmake && \
	make

ENTRYPOINT ["/opt/popart-1.7/src/popart"]
