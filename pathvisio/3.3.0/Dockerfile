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

WORKDIR /pathvisio
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y wget
RUN apt-get install -y openjdk-8-jdk unzip
RUN wget https://github.com/PathVisio/pathvisio/releases/download/v3.3.0/pathvisio_bin-3.3.0.zip
RUN unzip ./pathvisio_bin-3.3.0.zip
RUN rm ./pathvisio_bin-3.3.0.zip
WORKDIR /pathvisio/pathvisio-3.3.0
