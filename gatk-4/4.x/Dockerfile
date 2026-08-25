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

FROM ubuntu:22.04

ARG VERSION

RUN apt-get update && apt-get install -y wget unzip python3 openjdk-17-jre && \
    ln -s /usr/bin/python3 /usr/bin/python

RUN wget "https://github.com/broadinstitute/gatk/releases/download/${VERSION}/gatk-${VERSION}.zip" -O /tmp/gatk.zip && \
    unzip /tmp/gatk.zip -d /opt/ && \
    rm /tmp/gatk.zip && \
    cd "/opt/gatk-${VERSION}" && \
    ./gatk --version

ENV PATH="/opt/gatk-${VERSION}:${PATH}"