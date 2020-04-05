from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('memo.html')


## API 역할을 하는 부분
@app.route('/shopping', methods=['POST'])
def write_shopping():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.shopping.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


@app.route('/shopping', methods=['GET'])
def read_shopping():
    # 1.저장된리뷰를들 가져온다.
    shopping = list(db.shopping.find({}, {'_id': False}))
    # 2. 리뷰들을 돌려준다.
    return jsonify({'result': 'success', 'shopping': shopping})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
