FROM ubuntu:21.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential
RUN export DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/Europe/Lisbon /etc/localtime
RUN apt-get install -y tzdata    
RUN apt-get install -y software-properties-common && apt-get update
RUN apt-get install -y wget git python pip g++
ENV PATH="/usr/bin/:${PATH}"

#install Biopython
RUN pip3 install biopython
ENV PATH="/usr/local/lib/python3.9/dist-packages/:${PATH}"

#install freesasa
RUN pip3 install freesasa

#install ihm
RUN pip3 install ihm

WORKDIR /opt

#install HADDOCK-TOOLS    
RUN  git clone https://github.com/haddocking/haddock-tools

#install Reduce
RUN  wget https://github.com/rlabduke/MolProbity/raw/master/bin/linux/reduce
RUN cp /opt/reduce /opt/haddock-tools/ && cd /opt/haddock-tools && chmod 777 reduce
RUN g++ -o /opt/haddock-tools/contact-chainID /opt/haddock-tools/contact-chainID.cpp
RUN g++ -o /opt/haddock-tools/contact-segid /opt/haddock-tools/contact-segid.cpp 
ENV PATH="/opt/haddock-tools/:${PATH}"

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

WORKDIR /opt/haddock-tools
RUN chmod -R 777 *
