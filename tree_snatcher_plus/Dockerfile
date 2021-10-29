FROM ubuntu:14.04

RUN apt-get update && apt-get install -y software-properties-common wget unzip

RUN apt-get install -y openjdk-6-jre && rm -rf /var/lib/apt/lists/*

RUN wget https://www.cs.hhu.de/fileadmin/redaktion/Fakultaeten/Mathematisch-Naturwissenschaftliche_Fakultaet/Informatik/Computational_Cell_Biology/Folien/TreeSnatcherPlus_June2010_Linux.zip

RUN mkdir /opt/TreeSnatcherPlus

RUN unzip TreeSnatcherPlus_June2010_Linux.zip -d /opt

CMD java -jar -Dsun.java2d.opengl=true -Xms256m -Xmx1500m /opt/TreeSnatcherPlus.jar
