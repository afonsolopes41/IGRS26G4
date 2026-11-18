FROM ghcr.io/kamailio/kamailio:6.0.3-focal

USER root

RUN apt-get update && \
    apt-get install -y redis-tools python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install redis