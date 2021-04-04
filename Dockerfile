FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3-pip curl zip p7zip p7zip-full
RUN mkdir api/
COPY requirements.txt api/
RUN pip3 install -r api/requirements.txt

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
COPY credentials .aws/

COPY api.py api/

EXPOSE 55500

CMD ["python3", "api/api.py"]

