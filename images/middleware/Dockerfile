FROM cern/cc7-base
RUN yum install -y psmisc && \
    yum clean all && \
    rm -rf /var/cache/yum
ENV PYTHONPATH /code
COPY . /code

