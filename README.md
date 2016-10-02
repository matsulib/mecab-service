# MeCab Webサービス

docker-composeコマンドだけで起動できるMeCabサービス

* flask-mecab
    - MeCabを利用できるRESTfulなflaskサーバー
    - IPA辞書と新語辞書mecab-ipadic-neologdが選択できる

* フロントエンド
    - 未定

## ディレクトリ構成
```
.
├── README.md
├── docker-compose.yml
└── flask-mecab
    ├── Dockerfile
    ├── requirements.txt
    └── server.py

```

## 起動方法

```shell-session 
$ docker-compose up -d   
```

## 実行方法
HTTPリクエスト

```
POST /mecab/v1/parse-ipadic
POST /mecab/v1/parse-neologd
```

リクエストヘッダ

```
Content-Type: application/json
```

リクエストボディ

```
{
  "sentence": 文字列
}
```

## 実行例 ipadic
```shell-session
$ curl -X POST http://localhost:5000/mecab/v1/parse-ipadic \
       -H "Content-type: application/json" \
       -d '{"sentence": "関数型プログラミング"}'  | jq .
```

```
{
  "dict": "ipadic",
  "message": "Success",
  "results": [
    {
      "原型": "関数",
      "品詞": "名詞",
      "品詞細分類1": "一般",
      "品詞細分類2": "*",
      "品詞細分類3": "*",
      "活用型": "*",
      "活用形": "*",
      "発音": "カンスー",
      "表層形": "関数",
      "読み": "カンスウ"
    },
    {
      "原型": "型",
      "品詞": "名詞",
      "品詞細分類1": "接尾",
      "品詞細分類2": "一般",
      "品詞細分類3": "*",
      "活用型": "*",
      "活用形": "*",
      "発音": "ガタ",
      "表層形": "型",
      "読み": "ガタ"
    },
    {
      "原型": "プログラミング",
      "品詞": "名詞",
      "品詞細分類1": "サ変接続",
      "品詞細分類2": "*",
      "品詞細分類3": "*",
      "活用型": "*",
      "活用形": "*",
      "発音": "プログラミング",
      "表層形": "プログラミング",
      "読み": "プログラミング"
    }
  ],
  "status": 200
}
 
``` 

## 実行例 mecab-ipadic-neologd
mecab-ipadic-neologdは固有名詞に強い辞書です。

```shell-session
$ curl -X POST http://localhost:5000/mecab/v1/parse-neologd \
       -H "Content-type: application/json" \
       -d '{"sentence": "関数型プログラミング"}'  | jq .
```

```
{
  "dict": "neologd",
  "message": "Success",
  "results": [
    {
      "原型": "関数型プログラミング",
      "品詞": "名詞",
      "品詞細分類1": "固有名詞",
      "品詞細分類2": "一般",
      "品詞細分類3": "*",
      "活用型": "*",
      "活用形": "*",
      "発音": "カンスーガタプログラミング",
      "表層形": "関数型プログラミング",
      "読み": "カンスウガタプログラミング"
    }
  ],
  "status": 200
}
```