FROM python:3.8-slim-buster

ADD requirements.txt /requirements.txt
RUN pip3.8 install -r requirements.txt

ADD scripts/wait-for-it.sh /wait-for-it.sh
ADD brainstorm /brainstorm

EXPOSE 8000 5000