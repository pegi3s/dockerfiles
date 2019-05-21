# Don't forget to keep a delay between requests for at least 15 seconds or your IP address will be banned
# (see https://sppider.cchmc.org/sppider_doc.html#About)
# to see formfind information: cat ./opt/info

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y curl

COPY ./info ./opt/info
COPY ./run ./opt/run
RUN mkdir /data

WORKDIR /data
