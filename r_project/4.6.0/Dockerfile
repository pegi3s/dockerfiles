#
#   Copyright 2018-2025 Hugo López-Fernández, Miguel Reboiro-Jato,
#   Cristina P. Vieira, and Jorge Vieira
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

FROM ubuntu:26.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y build-essential ca-certificates software-properties-common apt-transport-https dirmngr gnupg wget && \
    add-apt-repository universe

ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add CRAN GPG key and the Ubuntu 26.04 (resolute-cran40) repository
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | gpg --dearmor -o /usr/share/keyrings/cran-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/cran-archive-keyring.gpg] https://cloud.r-project.org/bin/linux/ubuntu resolute-cran40/" > /etc/apt/sources.list.d/cran.list && \
    apt-get update

# Pin r-base packages and recommended dependencies to 4.6.0
RUN apt-get install -y \
    r-base-core=4.6.0* \
    r-recommended=4.6.0* \
    r-base=4.6.0* \
    r-base-dev=4.6.0*

WORKDIR /data
