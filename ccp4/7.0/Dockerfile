FROM ubuntu:16.04

RUN apt-get -qq update && apt-get -y upgrade
RUN apt-get -qq -y install vim tar sudo gcc g++ gfortran m4 tk8.4 tcl8.4 python2.7 git wget bzip2 tar expect
RUN apt-get -y install bc
RUN wget http://devtools.fg.oisin.rc-harwell.ac.uk/nightly/7.0/ccp4-7.0-linux64-latest.tar.bz2
RUN bunzip2 ccp4-7.0-linux64-latest.tar.bz2
RUN mkdir ./ccp4
RUN tar -xf ccp4-7.0-linux64-latest.tar -C ./ccp4 --strip-components=1

RUN touch $HOME/.agree2ccp4v6

COPY ./run /ccp4/bin
COPY ./functions /ccp4/bin

RUN chmod a+x /ccp4/bin/run

CMD ["ccp4/start"]
