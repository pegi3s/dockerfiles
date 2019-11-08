FROM ubuntu:18.04

RUN apt-get update \
	&& apt-get install -y wget libgtk2.0-0 libgconf-2-4 libcanberra-gtk*

WORKDIR /data

RUN wget https://www.megasoftware.net/releases/megax-cc_10.0.5-1_amd64.deb \
	&& dpkg -i megax-cc_10.0.5-1_amd64.deb \
	&& rm megax-cc_10.0.5-1_amd64.deb

ENTRYPOINT ["/usr/bin/megacc"]
