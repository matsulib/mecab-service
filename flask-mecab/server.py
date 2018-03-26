#!/bin/python3
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

import MeCab

app = Flask(__name__)
cors = CORS(app, resources={r"/mecab/*": {"origins": "*"}})

messages = ['Success', 'Faild']


@app.route('/mecab/v1/parse-ipadic', methods=['POST'])
def parse():
    if not (request.json and 'sentence' in request.json):
        abort(400)

    sentence = request.json['sentence']
    results = mecab_parse(sentence)

    return mecab_response(200, messages[0], results, 'ipadic')


@app.route('/mecab/v1/parse-neologd', methods=['POST'])
def parse_neologd():
    if not (request.json and 'sentence' in request.json):
        abort(400)

    sentence = request.json['sentence']
    results = mecab_parse(sentence, dic='neologd')

    return mecab_response(200, messages[0], results, 'neologd')


@app.errorhandler(400)
def error400(error):
    return mecab_response(400, messages[1], None, None)


def mecab_response(status, message, results, dic):
    return jsonify({'status': status, 'message': message, 'results': results, 'dict': dic}), status


def mecab_parse(sentence, dic='ipadic'):
    dic_dir = "/usr/local/lib/mecab/dic/"
    if dic == 'neologd':
        dic_name = 'mecab-ipadic-neologd'
    else:
        dic_name = dic

    m = MeCab.Tagger('-d ' + dic_dir + dic_name)

    # 出力フォーマット（デフォルト）
    format = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用形', '活用型','原型','読み','発音']

    return [dict(zip(format, (lambda x: [x[0]]+x[1].split(','))(p.split('\t')))) for p in m.parse(sentence).split('\n')[:-2]]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
