FROM ubuntu:16.04

WORKDIR /opt
RUN apt-get update \
  && apt-get install python3 python3-pip curl git sudo -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/taku910/mecab.git
WORKDIR /opt/mecab/mecab
RUN ./configure  --enable-utf8-only \
  && make \
  && make check \
  && make install \
  && ldconfig

WORKDIR /opt/mecab/mecab-ipadic
RUN ./configure --with-charset=utf8 \
  && make \
  &&make install

WORKDIR /opt/mecab
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /opt/mecab/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y

COPY . /opt/api
WORKDIR /opt/api
RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]
