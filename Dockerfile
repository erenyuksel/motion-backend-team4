FROM continuumio/miniconda3:24.1.2-0

RUN mkdir -p /backend
RUN mkdir -p /scripts
RUN mkdir -p /static-files
RUN mkdir -p /media-files

COPY ./scripts /scripts
RUN chmod -x /scripts

COPY ./backend/requirements.yml /backend/requirements.yml

RUN /opt/conda/bin/conda env create -f /backend/requirements.yml
ENV PATH /opt/conda/envs/motion/bin:$PATH

ENV PYTHONDONTWRITEBYTECODE=1

RUN echo "source activate motion" > ~/.bashrc


COPY ./backend /backend

WORKDIR /backend


