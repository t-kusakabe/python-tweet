FROM python:latest

ENV ROOT=/home/app
RUN mkdir $ROOT
WORKDIR $ROOT

COPY . $ROOT
RUN ["pip", "install", "requests", "requests_oauthlib"]

CMD ["python", "twitter.py"]
