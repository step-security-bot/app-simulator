# There is no arm64 version of mysql:5.7, so we use the amd64 version, until we migrate to mariadb.
# hadolint ignore=DL3029
FROM --platform=linux/amd64 mysql:5.7@sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb

LABEL org.opencontainers.image.source=https://github.com/cisco-open/app-simulator
LABEL org.opencontainers.image.description="mysql database for app-simulator"
LABEL org.opencontainers.image.licenses=BSD-3-Clause

RUN yum install -y php-cli && yum clean all

COPY setup.php /tmp/
COPY setup.sh /docker-entrypoint-initdb.d/
