#
#   Copyright 2018-2023 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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
RUN apt-get -y update
RUN apt-get install -y python3 python3-setuptools pip
RUN apt-get install -y unzip
RUN apt-get install -y bc
RUN apt-get install -y original-awk
RUN pip install wheel
WORKDIR /opt
COPY cport.zip /opt
RUN unzip cport.zip
RUN chmod -R 777 *
WORKDIR /opt/cport
RUN python3 setup.py develop
WORKDIR /opt
COPY cport_batch /opt
