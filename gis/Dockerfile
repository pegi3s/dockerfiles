FROM pegi3s/r_project

#Install GIS-specific packages

RUN apt-get install -y libgeos-dev
RUN Rscript -e "install.packages(c('raster', 'dismo', 'maptools', 'rgeos', 'rJava', 'jsonlite', 'sp'))"
RUN apt install -y texlive-extra-utils

COPY /gis /opt/gis
