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

FROM ubuntu:20.04

ARG VERSION

RUN apt-get update && apt-get install -y wget

RUN wget "https://github.com/GATB/TakeABreak/releases/download/v${VERSION}/TakeABreak-v${VERSION}-bin-Linux.tar.gz" -O /tmp/takeabreak.tar.gz && \
    tar zxvf /tmp/takeabreak.tar.gz -C /opt/ && \
    rm /tmp/takeabreak.tar.gz

ENV PATH="/opt/TakeABreak-v${VERSION}-bin-Linux/bin:${PATH}"
WORKDIR "/opt/TakeABreak-v${VERSION}-bin-Linux/bin"
