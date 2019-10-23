FROM ubuntu:18.04

RUN apt-get update \
	&& apt-get install -y build-essential wget libgtk2.0-0 libgconf-2-4 libcanberra-gtk* chromium-browser

WORKDIR /data

RUN wget https://www.megasoftware.net/releases/megax_10.0.5-1_amd64.deb \
  && dpkg -i megax_10.0.5-1_amd64.deb \
  && rm megax_10.0.5-1_amd64.deb

ENV PATH="/usr/lib/:$PATH"

ENTRYPOINT ["megax"]
