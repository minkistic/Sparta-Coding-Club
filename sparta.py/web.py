import flask
import pymongo

server = flask.Flask('내서버')
client = pymongo.MongoClient('localhost', 27017)

#만약 '/' 주소로 누군가 오면,
@server.route('/')
def home():
    # 'Hello World'를 출력하자
    return flask.render_template('index.html')

@server.route('/about')
def about():
    return flask.render_template('about.html')

@server.route('/users')
def users():
    user = [
        {'name':'곰튀김', 'gender':'M'},
        {'name': '곰튀김', 'gender': 'M'},
        {'name': '곰튀김', 'gender': 'M'},
        {'name': '곰튀김', 'gender': 'M'},
    ]
    return flask.jsonify(user)

@server.route('/movies')
def movies():
    #db에서 영화정보 꺼내서 json으로 제공하는 서버를 만들어주세요
    movies = list(client.sparta.movies.find({}, {'_id': False}))
    return flask.jsonify(movies)


server.run(port=5000, debug=True)
