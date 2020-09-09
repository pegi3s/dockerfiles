FROM pegi3s/lsd-base

# https://web.archive.org/web/20170916024357/http://www.markusbe.com:80/2009/09/about-running-32-bit-programs-on-64-bit-ubuntu-and-shared-libraries/
RUN apt-get install -y ia32-libs

ENV LD_LIBRARY_PATH=/usr/lib64/

COPY resources/sigdis.pl /opt/lineagesequencediscovery-master/sigdis/sigdis.pl

COPY resources/libraries/* /usr/lib/

RUN chmod +x /opt/lineagesequencediscovery-master/sigdis/*

RUN ln -s /usr/lib/libRmath.so /usr/lib/libRmath.so.1

RUN apt-get install -y tcl8.3

CMD /opt/lineagesequencediscovery-master/LSD.sh
