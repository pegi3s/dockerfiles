FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade
WORKDIR /opt
RUN apt-get install -y graphviz
ENV PATH="${PATH}:/usr/bin"
RUN apt-get install -y python3.8
RUN  apt-get install -y python3-pip
RUN  apt-get install -y xdg-utils chromium-browser.
RUN pip install graphviz
ENV PATH="${PATH}:/usr/local/lib/python3.8/dist-packages"
