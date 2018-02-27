FROM python:3.5-alpine
MAINTAINER Victor Schubert <victor@trackit.io>

RUN pip install --no-cache-dir python-nomad boto3
COPY cloudwatch-nomad-metrics.py ./cloudwatch-nomad-metrics.py
CMD ["./cloudwatch-nomad-metrics.py"]
