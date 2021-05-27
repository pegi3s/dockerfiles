#
#   Copyright 2018-2021 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN apt-get update && apt-get install -y gcc g++ perl python automake make \
                                       wget git curl libdb-dev \
                                       zlib1g-dev bzip2 libncurses5-dev \
                                       texlive-latex-base \
                                       default-jre \
                                       python-pip python-dev \
                                       gfortran \
                                       build-essential libghc-zlib-dev libncurses-dev libbz2-dev liblzma-dev libpcre3-dev libxml2-dev \
                                       libblas-dev gfortran git unzip ftp libzmq3-dev nano ftp fort77 libreadline-dev \
                                       libcurl4-openssl-dev libx11-dev libxt-dev \
                                       x11-common libcairo2-dev libpng12-dev libreadline6-dev libjpeg8-dev pkg-config libtbb-dev \
                   && apt-get clean

RUN curl -L https://cpanmin.us | perl - App::cpanminus

RUN cpanm install DB_File

RUN cpanm install URI::Escape


## set up tool config and deployment area:

ENV SRC /usr/local/src
ENV BIN /usr/local/bin

RUN apt-get install -y sqlite lighttpd libgd-tools libgd2-xpm-dev

RUN cpanm install GD
RUN cpanm install DBI
RUN cpanm install DBD::SQLite

RUN apt-get install -y software-properties-common

RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' && \
    apt-get update && \
    apt install -y mysql-server-5.6 && \
    apt install -y mysql-client-5.6 && \
    apt-get install -y libdbd-mysql-perl


## AUGUSTUS installation
WORKDIR /opt
RUN wget http://augustus.gobics.de/binaries/augustus.2.5.5.tar.gz && \
    tar xzvf augustus.2.5.5.tar.gz && \
    rm augustus.2.5.5.tar.gz && \
    cd augustus.2.5.5 && \
    make && \
    ln -s /opt/augustus.2.5.5 /opt/augustus && \
    cp /opt/augustus/src/consensusFinder /opt/augustus/bin/ && \
    cp /opt/augustus/src/curve2hints /opt/augustus/bin/

ENV PATH="/opt/augustus/bin/:/opt/augustus/scripts/:${PATH}"
ENV AUGUSTUS_CONFIG_PATH /opt/augustus/config/


## GMAP installation
WORKDIR $SRC
RUN wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2017-11-15.tar.gz && \
        tar xvf gmap-gsnap-2017-11-15.tar.gz && \
	rm gmap-gsnap-2017-11-15.tar.gz && \
        cd gmap-2017-11-15 && \
        ./configure && \
        make && \
        make install

## BLAT
WORKDIR $BIN
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat && \
        chmod 755 ./blat


## Fasta3
WORKDIR $SRC
RUN wget http://faculty.virginia.edu/wrpearson/fasta/fasta36/fasta-36.3.8g.tar.gz && \
        tar zxvf fasta-36.3.8g.tar.gz && \
	rm fasta-36.3.8g.tar.gz && \
        cd ./fasta-36.3.8g/src && \
        make -f ../make/Makefile.linux_sse2 all && \
        cp ../bin/fasta36 /usr/local/bin/fasta

       
## PASA installation
WORKDIR $SRC

ENV PASA_CO 6ea07cd

RUN git clone https://github.com/PASApipeline/PASApipeline.git && \
    cd PASApipeline && \
    git checkout $PASA_CO && \
    git submodule init && git submodule update && \
    make

ENV PASAHOME /usr/local/src/PASApipeline


# Fix PASA seqclean script location
RUN sed -i -e 's#seqclean/seqclean/seqclean#pasa-plugins/seqclean/seqclean/seqclean#g' /opt/augustus/scripts/autoAug.pl

# Create PASA conf.txt configuration file
RUN cat /usr/local/src/PASApipeline/pasa_conf/pasa.CONFIG.template > /usr/local/src/PASApipeline/pasa_conf/conf.txt

# Set Default MySQL Credentials on conf.txt configuration file
RUN sed -i -e 's#MYSQL_RW_USER=xxxxxx#MYSQL_RW_USER=user#g' /usr/local/src/PASApipeline/pasa_conf/conf.txt
RUN sed -i -e 's#MYSQL_RW_PASSWORD=xxxxxx#MYSQL_RW_PASSWORD=password#g' /usr/local/src/PASApipeline/pasa_conf/conf.txt
