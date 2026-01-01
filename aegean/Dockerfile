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

FROM fedora:32

RUN dnf -y update
RUN dnf -y install bc bzip2 findutils git lftp mlocate tcsh unzip zip wget which
RUN dnf -y install gcc-c++ make ruby cairo-devel pango-devel zlib-devel libnsl python3-pycurl python3-pyyaml python3-pandas python3-entrypoints python3-pytest python3-pytest-cov python3-biopython pandoc parallel
RUN ln -sf /usr/bin/python3 /usr/bin/python
WORKDIR /usr/local/src

#Installing the GenomeTools package
RUN git clone https://github.com/genometools/genometools.git
WORKDIR /usr/local/src/genometools
RUN make && make install && make clean && sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/genometools-x86_64.conf' && ldconfig

#Installing the cd-hit package
WORKDIR /usr/local/src
RUN git clone https://github.com/weizhongli/cdhit.git
WORKDIR /usr/local/src/cdhit
RUN make && make install

#Installing the lastz package
WORKDIR /usr/local/src/LASTZ
RUN wget http://www.bx.psu.edu/~rsharris/lastz/lastz-1.04.03.tar.gz && tar -xzf lastz-1.04.03.tar.gz
WORKDIR /usr/local/src/LASTZ/lastz-distrib-1.04.03/
RUN sed -i -e "1i LASTZ_INSTALL=/usr/local/bin" make-include.mak && sed -i -e "s/-Wall//;" src/Makefile && make && make install

#Installing AEGeAn
WORKDIR /usr/local/src
RUN git clone https://github.com/BrendelGroup/AEGeAn.git
WORKDIR /usr/local/src/AEGeAn
RUN make all LocusPocus && make install install-scripts && sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/aegean-x86_64.conf' && ldconfig

#Installing BLAST+ version 2.10.1 from NCBI
WORKDIR /usr/local/src
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.1/ncbi-blast-2.10.1+-x64-linux.tar.gz && tar -xzf ncbi-blast-2.10.1+-x64-linux.tar.gz
WORKDIR /usr/local/src/ncbi-blast-2.10.1+/bin
RUN cp * /usr/local/bin/
WORKDIR /usr/local/src
RUN rm ncbi-blast-2.10.1+-x64-linux.tar.gz

#Installing MuSeqBox version 5.7
WORKDIR /usr/local
RUN wget http://www.brendelgroup.org/bioinformatics2go/Download/MuSeqBox-5-7-2021.tar.gz && tar -xzf MuSeqBox-5-7-2021.tar.gz
WORKDIR /usr/local/MUSEQBOX5.7/src
RUN make linux && make install && make clean
WORKDIR /usr/local
RUN rm MuSeqBox-5-7-2021.tar.gz
RUN export LC_ALL=C
WORKDIR /data
