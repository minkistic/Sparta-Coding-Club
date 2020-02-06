import requests
import bs4

response = requests.get('https://finance.naver.com/sise/')
soup = bs4.BeautifulSoup(response.text, 'html.parser')


names = soup.select('div.box_type_r tr td.number')
for name in names:
    print(name.text)


    # siselist_tab_0 > tbody > tr:nth-child(3) > td:nth-child(4) > a