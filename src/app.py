import pymysql
from flask import Flask, redirect, url_for, request, render_template, json, jsonify
from flask_cors import CORS
import nltk
import time
import datetime

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

def AddRank(question):
    rankcursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT rank FROM ranking WHERE que=%s"
    rankcursor.execute(sql,question)
    rankvalue = rankcursor.fetchone()
    rankvalue['rank'] = rankvalue['rank'] + 1
    print(rankvalue['rank'])
    sql = "UPDATE ranking SET rank=%s WHERE que=%s"
    try:
        rankcursor.execute(sql,(int(rankvalue['rank']),question))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    

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
def NLP(sentence):
    NLP_cursor = db.cursor(pymysql.cursors.DictCursor)
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    key_word = [ i[0] for i in tagged if (i[1] == 'NNP' or i[1] == 'NN')]
    s = "Do you mean "
    for i in key_word:
        NLP_sql = "SELECT que FROM general_table WHERE que LIKE %s"
        ask = '%' + i + '%'
        NLP_cursor.execute(NLP_sql,ask)
        res = NLP_cursor.fetchall()
        print(res)
        if res is None:
            continue
        for j in res:
            s = s + '\n' + j['que']
    if s == "Do you mean ":
        return "No message"
    else:
        return s

def CHECK(question):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT ans FROM general_table WHERE que=%s"
    cursor.execute(sql, question)  # Input the order.return true if the order process successfully
    res = cursor.fetchone()  # get one info return the info
    cursor.fetchall()
    print(res)
    if (res is None) or (res['ans'] == ""):
        return NLP(question)
    else:
        AddRank(question)
        return res['ans']

HaveView = False

app = Flask("__name__")
CORS(app)


@app.route('/transfer', methods=["POST"])
def login():
    print(HaveView)
    respond = json.loads(request.get_data())  # get a dict
    print(respond['message'])
    ans = CHECK(respond['message'])
    print(ans)
    return jsonify({"ans": ans})

@app.route('/transfer', methods=["GET"])
def load():
    print(HaveView)
    rankcursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM ranking"
    rankcursor.execute(sql)
    ranklist = rankcursor.fetchall()
    print(ranklist)  # return a list (lie biao)
    return ranklist

@app.route('/login',methods=["GET"])
def req():
    global HaveView
    # print(HaveView)
    if HaveView == False:
        HaveView = True
        return jsonify({"situation":False})
    else:
        return jsonify({"situation":True})
@app.route('/sendhistory',methods=["POST"])
def saveHistory():
    response = json.loads(request.get_data())
    print(response)
    json_data = json.dumps(response)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "INSERT INTO history (msg,time) VALUES (%s,%s)"
    cursor.execute(sql,(json_data,datetime.datetime.now()))
    db.commit()
    return "success"

@app.route('/history',methods=["POST"])
def loadHistory():
    NowId = json.loads(request.get_data())
    print(NowId)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT msg FROM history WHERE id=%s"
    cursor.execute(sql,int(NowId))
    Nowmsg = cursor.fetchone()
    return Nowmsg['msg']

@app.route('/time',methods=["GET"])
def sendtime():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT id,time FROM history"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # 此处可自定义使用端口

# CHECK("What is Python")