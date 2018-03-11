FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install python3 python3-pip -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /opt/front
WORKDIR /opt/front
RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
