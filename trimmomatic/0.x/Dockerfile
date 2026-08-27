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

FROM eclipse-temurin:25-jre

ARG VERSION

RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*

RUN wget "https://github.com/usadellab/Trimmomatic/releases/download/v${VERSION}/Trimmomatic-${VERSION}.zip" -O /tmp/trimmomatic.zip && \
    mkdir -p /opt/trimmomatic && \
    unzip /tmp/trimmomatic.zip -d /opt/trimmomatic && \
    mv "/opt/trimmomatic/trimmomatic-${VERSION}.jar" /opt/trimmomatic/trimmomatic.jar && \
    rm /tmp/trimmomatic.zip

ENTRYPOINT ["java", "-cp", "/opt/trimmomatic/trimmomatic.jar", "org.usadellab.trimmomatic.Trimmomatic"]
CMD ["-version"]