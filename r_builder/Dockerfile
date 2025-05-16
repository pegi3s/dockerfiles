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

FROM pegi3s/docker:20.04

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    jq \
    bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY generate_dockerfile.sh /usr/local/bin/generate_dockerfile.sh
COPY list_r_packages.sh /resources/list_r_packages.sh

RUN chmod +x /usr/local/bin/generate_dockerfile.sh

CMD ["/bin/bash"]
