from flask import Flask, request, session, redirect, url_for, abort, render_template, flash
from flask_restful import reqparse, abort, Api, Resource
from konlpy.tag import Kkma
from konlpy.utils import pprint
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#이쪽 url로 post를 보내면 이 함수가 반응합니다
@app.route('/api/analyze-sentence', methods =['POST'])
def post_action():
    if request.method == 'POST':
        #json 데이터를 받습니다.
        json_data = request.get_json(); 
        print('json_data : {json_data}')

        #꼬꼬마 객체를 생성
        kkma = Kkma()
        #api 함수를 사용해 명사를 추출합니다
        nouns_list = kkma.nouns(json_data['sentence'])
        print(nouns_list)
        #list 자료구조를 json 형식으로 변환합니다.
        nouns_json = json.dumps(nouns_list)
        
        nouns_json = '{"result":' + nouns_json + "}"
        
        print(nouns_json)
        
        #명사들을 return 해줍니다
        return nouns_json
    return 'none POST!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='80') 
