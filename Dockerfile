FROM python:3.5-alpine
MAINTAINER Victor Schubert <victor@trackit.io>

RUN pip install --no-cache-dir python-nomad boto3
COPY nomadcloudwatch.py ./nomadcloudwatch.py
CMD ["./nomadcloudwatch.py"]
