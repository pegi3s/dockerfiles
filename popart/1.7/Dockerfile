FROM ubuntu:14.04

RUN apt-get update && apt-get install -y software-properties-common && \
	apt-get install -y libqt4-dev && \
	apt-get install -y libmarble-dev && \
	apt-get install -y lp-solve && \
	apt-get install -y liblpsolve55-dev && \
        apt-get install -y uuid-runtime && \
	apt-get install -y dbus

RUN apt-get update && apt-get install -y build-essential unzip wget

RUN wget http://popart.otago.ac.nz/software/popart-1.7.tar.bz2 -O /tmp/popart-1.7.tar.bz2 && \
	tar xvf /tmp/popart-1.7.tar.bz2 -C /opt/ && rm /tmp/popart-1.7.tar.bz2 && \
	sed -i '0,/\-llpsolve55 \-lmarblewidget/{s/\-llpsolve55 \-lmarblewidget/\-L\/usr\/lib\/lp_solve\/ \-llpsolve55 \-lmarblewidget \-ldl\n  QMAKE_RPATHDIR \+\= \/usr\/lib\/lp_solve\//}' /opt/popart-1.7/src/popart.pro && \
	cd /opt/popart-1.7/src && \
	qmake && \
	make

ENTRYPOINT ["/opt/popart-1.7/src/popart"]
