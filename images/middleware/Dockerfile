FROM centos
RUN yum install -y psmisc python3 && \
    yum clean all && \
    rm -rf /var/cache/yum
ENV PYTHONPATH /code
COPY . /code

