import requests
import bs4


# 밑에있는거 하나의 함수로 묶기라, count라는 함수 호출 인자("arument", "prameter")를 설정 가능


def get_song_ranks(count):
    # user-agent 복사 (소스에서 처음나오는거에 네트워크 > 헤더)
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    response = requests.get('https://music.naver.com/', headers=header)

    html = response.text

    soup = bs4.BeautifulSoup(html, 'html.parser')

    songs = soup.select('tr._track_dsc._tracklist_move')

    ranks = []  # rank에 하나씩 저장하기위해서 만듬

    for song in songs[:count]:
        rank = song.select_one('td.ranking span')
        title = song.select_one('td.name a')
        singer = song.select_one('td.artist a')

        # print(rank.text)
        # print(title.text)
        # print(singer.text)

        info = {
            'rank': rank.text,
            'title': title.text,
            'single': singer.text
        }
        # print(info)

        # rank에 하나씩 저장하기
        ranks.append(info)

    return ranks  # 함수돌린 결과 값을 가지고 있어라


r = get_song_ranks(3)  # 함수실행한 결과를 여기다 넣어라
print(r)
