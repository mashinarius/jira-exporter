FROM python:3.7-alpine

RUN mkdir /opt/app
RUN mkdir /opt/config

COPY ./config.py /opt/app/config.py
COPY ./jira_test.py /opt/app/jira_test.py
COPY ./prom.py /opt/app/prom.py

COPY ./requirements.txt /opt/requirements.txt

RUN pip install --upgrade -r /opt/requirements.txt

WORKDIR /opt/app

EXPOSE 8000
VOLUME ["/opt/config:rw"]
ENTRYPOINT ["python", "/opt/app/prom.py", "/opt/config/atlassian-exporter.ini"]
