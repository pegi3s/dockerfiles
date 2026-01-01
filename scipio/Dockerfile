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

FROM ubuntu:22.04
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y unzip wget gcc zlib1g-dev build-essential
COPY  scipio-1.4.zip /opt
WORKDIR /opt
RUN unzip scipio-1.4.zip
RUN apt-get install -y bioperl
RUN apt-get install -y libconfig-yaml-perl
WORKDIR /opt/scipio-1.4
RUN wget https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat
COPY main /opt/scipio-1.4
RUN chmod -R 777 *
ENV PATH="${PATH}:/opt/scipio-1.4"
