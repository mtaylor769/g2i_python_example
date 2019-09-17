FROM python:3.5.5-jessie
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# RUN apt-get update && apt-get -qq -y upgrade
# RUN apt-get -qq -y install apt-transport-https ca-certificates
# RUN apt-get -qq -y install curl vim python3 python-dev python3-dev python3-venv python-pip python-virtualenv libmysqlclient-dev mysql-client
RUN pip install --upgrade pip

WORKDIR /src
COPY . .
RUN pwd && ls -al

CMD ["/bin/bash/", "-c"]
ENTRYPOINT ["./docker-entrypoint.sh"]

