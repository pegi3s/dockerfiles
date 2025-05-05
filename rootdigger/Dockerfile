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

FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC && \
    apt-get install --assume-yes build-essential git cmake libopenblas-dev liblapacke-dev

RUN git clone https://github.com/computations/root_digger/ --depth=1 --recursive && \
    cd root_digger && make && cp bin/rd /usr/local/bin/