from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def post_order():
    name = request.form['name']
    HP = request.form['HP']
    add = request.form['add']
    quantity = request.form['quantity']
    money = request.form['money']

    print(HP, name, add, quantity, money)

    doc = {
        'name': name,
        'HP': HP,
        'add': add,
        'quantity': quantity,
        'money': money}

    db.sdgCustomer.insert_one(doc)

    return jsonify({'result': 'success', 'msg': 'Posting is completed'})


@app.route('/order', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    sdg_list = list(db.sdgCustomer.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'articles': sdg_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
