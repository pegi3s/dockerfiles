FROM ubuntu:16.04

RUN apt-get update --fix-missing \
    && apt-get install -y wget gcc make \
    && cd /usr/local/ \
    && wget http://abacus.gene.ucl.ac.uk/software/paml4.9h.tgz \
    && tar -xzvf paml4.9h.tgz \
    && rm -rf paml4.9h.tgz \
    && cd paml4.9h/src \
    && make \
    && cp baseml basemlg chi2 codeml evolver infinitesites mcmctree pamp yn00 /usr/local/bin/ \
    && cd /usr/local \
    && rm -rf /usr/local/paml4.9h \
    && apt-get remove -y wget gcc make \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /codeml

ENTRYPOINT ["codeml"]
