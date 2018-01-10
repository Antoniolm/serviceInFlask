FROM ubuntu:14.04

MAINTAINER Antonio David López Machado <antdlopma@gmail.com>
WORKDIR /app

ADD service.py /app/service.py
ADD dbSchema.sql /app/dbSchema.sql

RUN mkdir -p static

ADD static/style.css /app/static/style.css
ADD templates/index.html /app/templates/index.html

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN apt-get install -y git

RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RuN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN apt-get install -y mysql-server
RUN apt-get install -y libmysqlclient-dev

RUN pip install mysqlclient flask flask-mysqldb

ENTRYPOINT ["python"]
CMD ["service.py"]
