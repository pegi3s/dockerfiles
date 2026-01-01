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

FROM pegi3s/r_project

ENV version 2.21.5
ENV PICARD /usr/local/bin/picard/picard.jar

WORKDIR /usr/local/bin/picard/

RUN apt-get update -y && apt-get install -y \
    libnss-sss \
    openjdk-8-jre \
    curl \
    less \
    vim  \
    wget

RUN mkdir -p /usr/local/bin/picard \
    && curl -SL https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar \
    > /usr/local/bin/picard/picard.jar

RUN chmod 0644 /usr/local/bin/picard/picard.jar

ENTRYPOINT ["java", "-Dpicard.useLegacyParser=false", "-jar", "/usr/local/bin/picard/picard.jar"]
