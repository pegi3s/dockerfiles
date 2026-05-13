
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

# Base image with PyTorch + CUDA support
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Main working directory
WORKDIR /app

# Install git to clone the PeSTo repository
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the PeSTo repository into the image
RUN git clone https://github.com/LBM-EPFL/PeSTo.git /app/pesto

# Move into the PeSTo project folder
WORKDIR /app/pesto

# Install Python dependencies and nbconvert
RUN pip install --no-cache-dir -r requirements.txt nbconvert

# Convert the main notebook into a python script
RUN jupyter nbconvert --to script apply_model.ipynb

# Copy custom helper scripts into the image
COPY entrypoint.sh /app/entrypoint.sh
COPY run_pesto.py /app/pesto/run_pesto.py
COPY make_csv.py /app/pesto/make_csv.py

# Make the entrypoint script executable 
RUN chmod +x /app/entrypoint.sh

# Run the worflow through the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]