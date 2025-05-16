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

FROM ubuntu:16.04

ADD http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz /opt

RUN ln -s /opt/FLASH-1.2.11-Linux-x86_64/flash /usr/bin

RUN cd /opt && \
	tar -xvzf FLASH-1.2.11-Linux-x86_64.tar.gz && \
	rm FLASH-1.2.11-Linux-x86_64.tar.gz
	
ENV PATH="/opt/FLASH-1.2.11-Linux-x86_64/:${PATH}"

ENTRYPOINT ["flash"]
