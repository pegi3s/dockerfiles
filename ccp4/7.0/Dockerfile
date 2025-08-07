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

RUN apt-get -qq update && apt-get -y upgrade
RUN apt-get -qq -y install vim tar sudo gcc g++ gfortran m4 tk8.4 tcl8.4 python2.7 git wget bzip2 tar expect
RUN apt-get -y install bc
RUN wget http://devtools.fg.oisin.rc-harwell.ac.uk/nightly/7.0/ccp4-7.0-linux64-latest.tar.bz2
RUN bunzip2 ccp4-7.0-linux64-latest.tar.bz2
RUN mkdir ./ccp4
RUN tar -xf ccp4-7.0-linux64-latest.tar -C ./ccp4 --strip-components=1

RUN touch $HOME/.agree2ccp4v6

COPY ./run /ccp4/bin
COPY ./functions /ccp4/bin

RUN chmod a+x /ccp4/bin/run

CMD ["ccp4/start"]
