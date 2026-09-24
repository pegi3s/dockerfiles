
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

# Dockerfile for the SCRIBER client script
#
# Submits a PDB chain to the SCRIBER web server and retrieves predictions.
# Based on the cport-like project: https://github.com/pegi3s/dockerfiles/tree/master/cport-like
#
# Build:
#   docker build -t scriber/pegi3s .
#
# Run:
#   docker run --rm \
#     -v /path/to/your/data:/data \
#     -v /path/to/output:/output \
#     scriber-client /data/protein.pdb A --output /output/scriber_results.csv

FROM python:3.11-slim

# Install OS-level dependencies required by Biopython / lxml
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        libxml2-dev \
        libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
        mechanicalsoup \
        pandas \
        biopython \
        requests \
        lxml

WORKDIR /app

# Copy the SCRIBER client script into the image
COPY run_scriber.py /app/run_scriber.py

# Default data / output mount points
VOLUME ["/data", "/output"]

ENTRYPOINT ["python", "/app/run_scriber.py"]
