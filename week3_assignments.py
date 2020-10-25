import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
res = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

if res.status_code == 200:
    client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
    db = client.musicChart
    soup = BeautifulSoup(res.text, 'html.parser')
    dataList = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    for data in dataList:
        rank = data.select_one('td.number').text.split(' ')[0].strip()
        title = data.select_one('td.info > a.title.ellipsis').text.strip()
        singer = data.select_one('td.info > a.artist.ellipsis').text.strip()

        doc = {'rank': rank, 'title': title, "artist": singer}
        db.musicChart.insert_one(doc)

        print(rank, title, singer)
else:
    print('Failed to get the HTML Contents')
