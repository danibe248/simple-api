FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3-pip
RUN mkdir api/
COPY requirements.txt api/
RUN pip3 install -r api/requirements.txt

COPY config.json api/
COPY api.py api/
COPY Encoder.py api/

EXPOSE 55500

CMD ["python3", "api/api.py"]

