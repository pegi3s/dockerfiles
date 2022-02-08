#
#   Copyright 2018-2022 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

FROM ubuntu:21.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential && \
    export DEBIAN_FRONTEND=noninteractive && \
    ln -fs /usr/share/zoneinfo/Europe/Lisbon /etc/localtime && \
    apt-get install -y tzdata software-properties-common wget git python pip g++ tar

ENV PATH="/usr/bin/:${PATH}"

RUN pip3 install biopython freesasa ihm
ENV PATH="/usr/local/lib/python3.9/dist-packages/:${PATH}"

RUN cd /opt && \
    git clone https://github.com/haddocking/haddock-tools.git && \
    cd /opt/haddock-tools && \
    git checkout d5e7bb33853464250b93692ce20a81826ce15d94

ENV PATH="/opt/haddock-tools/:${PATH}"

RUN wget https://github.com/rlabduke/MolProbity/raw/master/bin/linux/reduce -O /opt/haddock-tools/reduce && \
    chmod 777 /opt/haddock-tools/reduce

RUN g++ -o /opt/haddock-tools/contact-chainID /opt/haddock-tools/contact-chainID.cpp
RUN g++ -o /opt/haddock-tools/contact-segid /opt/haddock-tools/contact-segid.cpp

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

WORKDIR /opt/haddock-tools

RUN chmod -R 777 *

WORKDIR /data
