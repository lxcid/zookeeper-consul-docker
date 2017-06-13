FROM zookeeper:3.4

ENV CONSUL_TEMPLATE_VERSION 0.18.5
ENV CONSUL_VERSION=0.8.4
ENV NEXTID_VERSION 1.0.0

RUN set -x && \
    apk add --no-cache ca-certificates curl gnupg libcap openssl && \
    wget \
      -q https://github.com/lxcid/nextid/releases/download/v${NEXTID_VERSION}/nextid.jar \
      -O /usr/local/bin/nextid.jar && \
    wget \
      -q https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip \
      -O /tmp/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    unzip -d /usr/local/bin /tmp/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    rm /tmp/consul_${CONSUL_VERSION}_linux_amd64.zip && \
    wget \
      -q https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
      -O /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    unzip -d /usr/local/bin /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    rm /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip
