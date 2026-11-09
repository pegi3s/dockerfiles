#
#   Copyright 2018-2026 Hugo López-Fernández, Miguel Reboiro-Jato,
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

FROM pegi3s/docker:29.0.1

# Install dependencies (Java for Nextflow, curl to download, git to clone the pipeline)
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    ca-certificates \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Nextflow (pinned: the pipeline config requires 25.04.6 and 26.x rejects it)
# and clone the pipeline
RUN git clone --depth 1 https://github.com/hillerlab/make_lastz_chains /opt/make_lastz_chains \
    && curl -fsSL https://github.com/nextflow-io/nextflow/releases/download/v25.10.8/nextflow -o /usr/local/bin/nextflow \
    && chmod +x /usr/local/bin/nextflow

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["bash"]
