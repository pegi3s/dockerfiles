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

RUN apt-get update && apt-get install -y --no-install-recommends wget \
        unzip gcc build-essential time python python-pip python-setuptools \
        locales make python-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install awscli

RUN wget http://eddylab.org/software/hmmer/hmmer-3.2.1.tar.gz && \
        tar -xzf hmmer-3.2.1.tar.gz && cd hmmer-3.2.1 && \
        ./configure && make && make install && \
        cd .. && rm -r hmmer-3.2.1 hmmer-3.2.1.tar.gz

WORKDIR /usr/local/bin

RUN wget http://tandem.bu.edu/trf/downloads/trf409.linux64 && \
        mv trf*.linux64 trf && chmod +x trf

RUN wget http://www.repeatmasker.org/rmblast-2.10.0+-x64-linux.tar.gz && \
    tar -zxvf rmblast-2.10.0+-x64-linux.tar.gz && \
    rm rmblast-2.10.0+-x64-linux.tar.gz && \
    cp /usr/local/bin/rmblast-2.10.0/bin/* /usr/local/bin && \
    rm -R /usr/local/bin/rmblast-2.10.0

WORKDIR /usr/local

RUN wget http://repeatmasker.org/RepeatMasker-open-4-0-9-p2.tar.gz && \
    tar -xzvf RepeatMasker-open*.tar.gz && rm -f RepeatMasker-open*.tar.gz

WORKDIR /usr/local/RepeatMasker/Libraries

RUN wget https://www.dfam.org/releases/Dfam_3.1/families/Dfam.hmm.gz
RUN rm Dfam.hmm && gunzip Dfam.hmm.gz

WORKDIR /usr/local/RepeatMasker

RUN perl ./configure -trfbin=/usr/local/bin/trf -hmmerbin=`which nhmmscan`
RUN perl ./configure -trfbin=/usr/local/bin/trf -rmblastbin=`which rmblastn`

RUN cpan Text::Soundex

ENV PATH=/usr/local/RepeatMasker:$PATH
ENV PATH=/usr/local/bin:$PATH

ADD add_lib /usr/local/RepeatMasker

WORKDIR /data
