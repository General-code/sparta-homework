import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
res = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = bs(res.text, 'html.parser')
dataList = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for data in dataList:
    rank = data.select_one('td.number').text.split(' ')[0].strip()
    title = data.select_one('td.info > a.title.ellipsis').text.strip()
    singer = data.select_one('td.info > a.artist.ellipsis').text.strip()

    print(rank, title, singer)
