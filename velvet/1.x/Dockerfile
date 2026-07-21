#
#   Copyright 2018-2026 Hugo López-Fernández, Miguel Reboiro-Jato, Cristina
#   P. Vieira, and Jorge Vieira
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

FROM ubuntu:24.04

ARG VERSION

RUN apt-get update && apt-get install -y wget build-essential zlib1g-dev

RUN wget "https://github.com/dzerbino/velvet/archive/v${VERSION}.tar.gz" -O /tmp/velvet.tar.gz && \
    tar zxvf /tmp/velvet.tar.gz -C /opt/ && rm /tmp/velvet.tar.gz && \
    cd "/opt/velvet-${VERSION}" && \
    make && \
    cp velveth velvetg /usr/local/bin/
