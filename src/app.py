import pymysql
from flask import Flask, redirect, url_for, request, render_template, json, jsonify
from flask_cors import CORS
import nltk

import json

'''
app = Flask(__name__)
@app.route('/<name>')
def hello_world(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run()
'''

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='913913',
    database='GENERAL',
    charset='utf8',
)


# INSERT INFORMATION

def INSERTMESSAGE(question, answer):
    cursor = db.cursor();
    sql = """INSERT INTO general_table(que,ans)
    VALUES 
    ( %s , %s )"""
    try:
        cursor.execute(sql, (question, answer))  # success!    THE STRING IS %s
        db.commit()
    except:
        print('插入数据失败！')  # INSERT A INFO WHICH HAS EXISTED WILL GET A ERROR

        db.rollback()

    db.close()


# CHECK INFORMATION         SUCCESS!
def CHECK(question):
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT ans FROM general_table WHERE que=%s"
    cursor.execute(sql, question)  # Input the order.return true if the order process successfully
    cursor.scroll(0, 'absolute')
    res = cursor.fetchone()  # get one info return the info
    print(res)
    if res['ans'] == "":
        return "No Message"
    else:
        return res['ans']


app = Flask("__name__")
CORS(app)


@app.route('/transfer', methods=["POST", "GET"])
def login():
    respond = json.loads(request.get_data())  # get a dict
    print(respond['message'])
    ans = CHECK(respond['message'])
    print(ans)
    return jsonify({"ans": ans})


'''# we usually use POST for login
@app.route('/', methods=["POST","GET"]) # GET
def index():
    return render_template('login.html')   # load the login.html web
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # 此处可自定义使用端口
# CHECK("What is Python")
'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/successs/<name>')
def success(name):
    return 'welcome %s' % name
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        print(1)
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        print(2)
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
if __name__ == '__main__':
    app.run()
'''
