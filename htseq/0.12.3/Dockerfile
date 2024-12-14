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
