FROM python:latest
MAINTAINER Toni Grigoriu <toni@grigoriu.ro>
RUN mkdir /opt/ini_parser
COPY parse.py /opt/ini_parser
WORKDIR /opt/ini_parser
ENTRYPOINT ["python", "parse.py"]
