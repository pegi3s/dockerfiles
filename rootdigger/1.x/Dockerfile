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

ARG VERSION

RUN apt-get update && \
    apt-get upgrade --assume-yes && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC && \
    apt-get install --assume-yes build-essential git cmake libatlas-base-dev liblapacke-dev

# At v1.8.0 the source defines RD_COMPILE_DEFS but never applies it to the
# target, so the built binary reports "GIT_REV" instead of the version. This
# line applies the upstream fix (present in later commits).
RUN git clone --branch v${VERSION} --recursive \
      https://github.com/computations/root_digger.git /opt/root_digger && \
    cd /opt/root_digger && \
    sed -i '/target_link_libraries(rd PRIVATE/a target_compile_definitions(rd PRIVATE ${RD_COMPILE_DEFS})' src/CMakeLists.txt && \
    make && \
    cp bin/rd /usr/local/bin/
