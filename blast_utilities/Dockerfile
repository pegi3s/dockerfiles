FROM pegi3s/blast:2.6.0-1

ADD scripts /opt/scripts

RUN chmod 777 /opt/scripts/*

ENV PATH="/opt/scripts:${PATH}"
