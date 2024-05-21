FROM pegi3s/cport:2024.05

RUN apt-get install -y bc

WORKDIR /
COPY cport_batch /
RUN chmod -R 777 /cport_batch
