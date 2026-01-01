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

FROM ubuntu:20.04

WORKDIR /app
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential gfortran git wget unzip
RUN apt-get install -y python3.8 python3-pip
RUN pip3 install cython numpy scipy matplotlib


# 3seq 
RUN mkdir /git ; \ 
cd /git && \
git clone https://gitlab.com/lamhm/3seq && \
cd 3seq && \
make

# geneconv
RUN mkdir /scratch ; \
cd /scratch && \
wget https://www.math.wustl.edu/~sawyer/geneconv/unix.source.tar.gz && \
tar -xzf unix.source.tar.gz && \
cd unix.source && \
gcc -DUNIX -o geneconv -O3 geneconv.c version.c vcalc.c vtcalc.c \
  vsetopts.c vread.c vdump.c vutil.c -lm

#openrdp
WORKDIR /git
RUN git clone https://github.com/PoonLab/OpenRDP
WORKDIR /git/OpenRDP
RUN rm -rf Dockerfile docker
RUN cd /git/OpenRDP && python3 setup.py install
RUN chmod 777 /git/OpenRDP/tests/*

#phipack
WORKDIR /phipack
RUN wget https://www.maths.otago.ac.nz/~dbryant/software/PhiPack.tar -O /tmp/PhiPack.tar && \
    tar -xvf /tmp/PhiPack.tar && \
    rm /tmp/PhiPack.tar -f && \
    cd /phipack/PhiPack/src && \
    make

COPY config /app
COPY recombine /app

WORKDIR /app

