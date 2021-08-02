#FROM python:3.8-alpine3.13
FROM python:3.8-slim-buster

WORKDIR /opt/app
COPY . .
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pandas tabulate

ENTRYPOINT [ "bash" ]
