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

FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
WORKDIR /opt
RUN apt-get install -y graphviz
ENV PATH="${PATH}:/usr/bin"
RUN apt-get install -y python3.8
RUN  apt-get install -y python3-pip
RUN  apt-get install -y xdg-utils chromium-browser.
RUN pip install graphviz
ENV PATH="${PATH}:/usr/local/lib/python3.8/dist-packages"
