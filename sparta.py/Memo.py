#메모장을 위한 서버를 만드는 과정입니다.
# 서버시작: mongod --dbpath ~/data/db

#HTML을 주는 API: 기본 실행
#HTML을 주는 API: HTML 파일 불러오기 -> render_template

from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient           # pymongo를 임포트 하기

import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('memo.html')

@app.route('/bookmark', methods=['POST'])
def bookmark_post():
    #  db에 저장한다.
    try:  # 이걸 시도해봐 우선
        # 1. 클라이언트가 보내준 url을 받기
        url = request.form['url']

        # 2. 그 url의 내용을 가져오기
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url, headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        # 3. 그 url의 내용에서 title, image, desc 을 찾아오기 (bs4)
        url_image = og_image['content']
        url_title = og_title['content']
        url_description = og_description['content']

        # 4. 그래서 그걸로 doc 을 만들자
        doc = {
            'title': url_title,
            'image': url_image,
            'desc': url_description,
            'url': url,
        }
        db.bookmarks.insert_one(doc)
    except: #시도한게 안되면 이걸해
        return jsonify({'result': 'fail', 'msg': '이 요청은 POST!'})

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/bookmark', methods=['GET'])
def bookmark_get():
    #db에서 읽어온다.
    bookmarks = list(db.bookmarks.find({}, {'_id':False})) #db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(bookmarks) #제이슨 형식으로 만들어라


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)