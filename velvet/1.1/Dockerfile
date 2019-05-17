FROM continuumio/miniconda3

RUN conda config --add channels bioconda
RUN conda install -c bioconda velvet
RUN conda create -n velvet_env velvet

ENV PATH=$PATH:/opt/conda/envs/velvet_env/bin
