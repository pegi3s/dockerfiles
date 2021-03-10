ARG biopython_version

FROM pegi3s/biopython:${biopython_version}

ADD scripts /opt/scripts

RUN chmod 777 /opt/scripts/*

ENV PATH="/opt/scripts:${PATH}"
