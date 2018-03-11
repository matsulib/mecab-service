import os
import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
FLASK_MECAB_URI= os.getenv('FLASK_MECAB_URI', '')


@app.route('/')
def index():
    return render_template('index.html',
        title='形態素解析ページ',
        FLASK_MECAB_URI=FLASK_MECAB_URI)


@app.route('/api/<dict>', methods=['POST'])
def api(dict):
    return requests.post('/'.join([FLASK_MECAB_URI, dict]),
                        headers={'Content-type': 'application/json'},
                        data=json.dumps(request.json)).text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
