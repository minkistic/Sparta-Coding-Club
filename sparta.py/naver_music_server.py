# import requests
# import bs4

# 서버를만드는 법
import flask
#다른파일에서 임포트
import naver_music_crawler


app = flask.Flask('네이버뮤직 순위 서버')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/music', methods=['POST'])
def music():
    return "POST Music"

@app.route('/music', methods=['GET'])
def music():
    try:
        c = flask.request.args['count']
    except: #에러 날 상황을 세
        c = 5
    # print(flask.request.args['info'])
    data = naver_music_crawler.get_song_ranks(int(c))
    return flask.jsonify(data)


app.run(port=5000, debug=True)



