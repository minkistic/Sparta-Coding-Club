import requests
import bs4
import pymongo

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

response = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908', headers = headers)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

client = pymongo.MongoClient('localhost', 27017)

ranks = soup.select('table.list_wrap tr')
for rank in ranks:
    number = rank.select_one('list.td number')
    song = rank.select_one('list.info title ellipsis')
    singer = rank.select_one('list.info artist ellipsis')
    if number is not None:
        top = {'number': float(number.text),
               'song': song.text,
               'singer': singer.text}
        client.sparta.top50.insert_one(top)

#db에서 모든 영화 정보 읽기
top50 = client.sparta.top50

top50_list = list(top50.find())
for top in top50_list:
    print(top)

#순위 / 곡 제목 / 가수
