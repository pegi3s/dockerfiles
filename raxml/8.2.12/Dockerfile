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

RUN apt-get update && apt-get install -y wget make gcc

RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz -O /tmp/v8.2.12.tar.gz && \
    tar -xvzf /tmp/v8.2.12.tar.gz -C /opt/ && \
    rm /tmp/v8.2.12.tar.gz && \
	cd /opt/standard-RAxML-8.2.12 && \
    make -f Makefile.gcc  && \
    rm *.o  && \
    make -f Makefile.SSE3.gcc  && \
    rm *.o  && \
    make -f Makefile.PTHREADS.gcc  && \
    rm *.o  && \
    make -f Makefile.SSE3.PTHREADS.gcc  && \
    rm *.o  && \
    cp raxmlHPC* /usr/local/bin
