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

FROM python:2.7.18

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y unzip wget

RUN python2.7 -m pip install --user numpy pysam
	
RUN wget https://files.pythonhosted.org/packages/61/7b/7a31e09ced6994d704d696c28b2c85c12d0653ffcfd4a21a3c231e7f58a6/HTSeq-0.12.3.tar.gz -O /tmp/htseq.tar.gz && \
    tar zxvf /tmp/htseq.tar.gz -C /opt/ && \
    rm /tmp/htseq.tar.gz -f && \
    cd /opt/HTSeq-0.12.3/ && \
    python setup.py install --user && \
    chmod +x scripts/htseq*

ENV PATH=/opt/HTSeq-0.12.3/scripts/:${PATH}
