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

FROM ubuntu:16.04
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gcc zip make g++ wget
WORKDIR /opt
RUN wget https://sourceforge.net/projects/kakscalculator2/files/KaKs_Calculator2.0.tar.gz
COPY ./KaKs_Calculator2.0.tar.gz /opt/KaKs_Calculator2.0.tar.gz
RUN tar zxvf KaKs_Calculator2.0.tar.gz && rm KaKs_Calculator2.0.tar.gz
WORKDIR /opt/KaKs_Calculator2.0/src
RUN sed -i '21i #include <string.h>' base.h
RUN make
COPY ./FASTA-AXT /opt/KaKs_Calculator2.0/src/FASTA-AXT
RUN chmod 777 /opt/KaKs_Calculator2.0/src/FASTA-AXT
ENV PATH="/opt/KaKs_Calculator2.0/src/:${PATH}"
