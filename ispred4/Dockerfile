
#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira,
#   Miguel Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
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

# LABEL contributor="pegi3s"

#   Based on the cport-like project:
#   https://github.com/pegi3s/dockerfiles/tree/master/cport-like
#
#   Licensed under the Apache License, Version 2.0
#

FROM python:3.11-slim

# Install system dependencies required by mechanicalsoup / lxml
RUN apt-get update && apt-get install -y --no-install-recommends \
        libxml2 \
        libxslt1.1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
        mechanicalsoup \
        pandas \
        lxml \
        requests

# Copy the prediction script into the image
COPY ispred4.py /app/ispred4.py

# Working directory exposed to the host via a volume mount
WORKDIR /data

# Default entry point — users can pass extra arguments after the image name
ENTRYPOINT ["python", "/app/ispred4.py"]
# Default: scan /data for *.pdb files and use chain A
CMD ["--data-dir", "/data", "--chain", "A"]
