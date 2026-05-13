
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

FROM ubuntu:22.04

LABEL description="PIPENN-EMB: Protein Interface Prediction with ProtT5 Embeddings"

ENV DEBIAN_FRONTEND=noninteractive \
    PIPENN_HOME=/opt/pipenn/ \
    PYTHONPATH=/opt/pipenn

ENV TF_CPP_MIN_LOG_LEVEL=2
ENV CUDA_VISIBLE_DEVICES=""
ENV TF_ENABLE_ONEDNN_OPTS=0

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev git wget dssp && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 1. Upgrade pip and handle core typing
RUN python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    python3 -m pip install --no-cache-dir "typing_extensions>=4.10.0"

# 2. Install dependencies with pinned NumPy and modern TensorFlow
# We pin numpy<2.0.0 to avoid the 'ComplexWarning' / 'numpy.core' breaking changes
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir \
    "numpy<2.0.0" \
    "pandas<2.1.0" \
    "scikit-learn==1.3.0" \
    "tensorflow==2.15.1" \
    "transformers" \
    "sentencepiece" \
    "joblib" \
    "matplotlib" \
    "psutil" \
    "xgboost" \
    "treelib" \
    "shap" \
	"comet_ml" \
	"plotly" \
    "kaleido" \
	"biopython"

RUN git clone https://github.com/ibivu/pipenn.git "$PIPENN_HOME"

# 3. Patch PIPENN script for CPU and EMB mode
RUN sed -i '1i import os\nos.environ["CUDA_VISIBLE_DEVICES"] = "-1"' "$PIPENN_HOME/dnet-ppi/dnet-XD-ppi-keras.py" && \
    sed -i "s/ONLY_TEST = False/ONLY_TEST = True/g" "$PIPENN_HOME/dnet-ppi/dnet-XD-ppi-keras.py" && \
    sed -i "s/datasetLabel = 'Biolip_N'/datasetLabel = 'Biolip_P'/g" "$PIPENN_HOME/dnet-ppi/dnet-XD-ppi-keras.py" && \
    sed -i "s/ONE_HOT_ENCODING = True/ONE_HOT_ENCODING = False/g" "$PIPENN_HOME/dnet-ppi/dnet-XD-ppi-keras.py"

# 4. Download Model Weights (PIPENN-EMB model trained with ProtT5 embeddings, expects 1025 features)
RUN mkdir -p "$PIPENN_HOME/models/all-models/biolip-p/" && \
    wget -O "$PIPENN_HOME/models/all-models/biolip-p/dnet-ppi-model.hdf5" \
    https://www.ibi.vu.nl/downloads/PIPENN/PIPENN/Pretrained-Models/Embedding-Models/biolip-p/dnet-ppi-model.hdf5

# 5. Pre-download ProtT5 (11GB)
# This should now work without the NumPy error
RUN python3 -c 'from transformers import T5EncoderModel, T5Tokenizer; \
    T5EncoderModel.from_pretrained("Rostlab/prot_t5_xl_uniref50"); \
    T5Tokenizer.from_pretrained("Rostlab/prot_t5_xl_uniref50")'

# Set the PYTHONPATH so predict.py can import PIPENN modules directly
ENV PYTHONPATH="/opt/pipenn:/opt/pipenn/utils:${PYTHONPATH}"

# Copy the new predict.py
COPY predict.py /usr/local/bin/predict_ppi
RUN chmod +x /usr/local/bin/predict_ppi

WORKDIR "$PIPENN_HOME"
ENTRYPOINT ["python3", "/usr/local/bin/predict_ppi"]