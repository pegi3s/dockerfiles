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

RUN apt-get update --fix-missing \
    && apt-get install -y wget gcc make \
    && cd /usr/local/ \
    && wget http://abacus.gene.ucl.ac.uk/software/SoftOld/paml4.9h.tgz \
    && tar -xzvf paml4.9h.tgz \
    && rm -rf paml4.9h.tgz \
    && cd paml4.9h/src \
    && make \
    && cp baseml basemlg chi2 codeml evolver infinitesites mcmctree pamp yn00 /usr/local/bin/ \
    && cd /usr/local \
    && rm -rf /usr/local/paml4.9h \
    && apt-get remove -y wget gcc make \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /codeml

ENTRYPOINT ["codeml"]
