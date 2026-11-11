FROM pegi3s/docker:29.0.1

RUN apt-get update && apt-get -y upgrade

COPY run_all run_align matrix_inverted txt_to_meg common infer_UPGMA_distances.mao /opt/

WORKDIR /opt

RUN chmod 777 run_all run_align matrix_inverted txt_to_meg common

ENTRYPOINT ["./run_all"]

