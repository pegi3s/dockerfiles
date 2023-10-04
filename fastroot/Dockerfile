FROM python:3.9

RUN pip install --upgrade pip && \
    pip install --no-cache-dir FastRoot==1.5 treeswift==1.1.14 cvxopt==1.2.5 numpy==1.26.0

RUN apt-get update -y && \
    apt-get install dos2unix && \
    dos2unix /usr/local/bin/FastRoot.py && \
    apt-get remove -y dos2unix

ENTRYPOINT ["FastRoot.py"]
