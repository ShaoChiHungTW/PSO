# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 14:05:07 2017

@author: Kiki Hung
"""

from flask import Flask
from flask.ext.wtf import Form
from flask import request
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask import render_template
#db SQL
from transwarp import db


app = Flask(__name__)
#from app import views
#from app import app
#@app.route("/")
#def hello():
#    return "HEY KIKI"

#get：[菜單]取得我們想要的資料
#post：[點菜]新增一項資料
#put：[把漢堡改成薯條]覆蓋舊有資料
#patch：[加點薯條]附加新的資料
#delete：[不吃了]刪除資料

#存取對象登入
#@app.route('/', methods = [ 'GET', 'POST' ])  

#jinjia2
#Homepage


@app.route('/')
def Signin_Form():
    return render_template('form.html')
#'''<form action="/signin" method="post">
#                <h1>BenQQQQQQ</h1>
#                <samp>Account</samp>
#                <p><input name = "username"></p>
#                <samp>Password</samp>
#                <p><input name = "password" type = "password"></p>
#                <p><button type = "submit"><b>Sign In</b></button></p>
#                </form>'''


#從Request對象讀取內容
@app.route('/', methods = ['post' ])
def SignIn():
    username = request.form['username']
    password = request.form['password']
    #先預設admin/password
    if username == 'admin' and password == 'password':
        return render_template('SigninOk.html', username = username)
    return render_template('form.html', message = 'Please check your username or password', username = username)
    
#    if request.form['username'] == 'admin' and request.form['password'] == 'password':
#        return '<h3>Hello, admin!</h3>'
#    #else
#    return '<h3>Please check your username or password.</h3>'   

#數據庫
db.create_engine(user = 'root', password = 'password', database = 'test', host = '127.0.0.1', port = 3306)
#查詢
users = db.select('select * from user')
# users =>
# [
#     { "id": 1, "name": "Michael"},
#     { "id": 2, "name": "Bob"},
#     { "id": 3, "name": "Adam"}
# ]
n = db.update('insert into user(id, name) values(?, ?)', 4, 'Kiki')
#統一以?作為佔位符
with db.connection():
    db.select('...')
    db.update('...')
    db.update('...')
with db.transaction():
    db.select('...')
    db.update('...')
    db.update('...')

#數據庫引擎對象
class _Engine(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self._connect()

engine = None

#持有數據庫的上下文對象
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transactions = 0
    

#表單
class ParameterForm(Form):
   Parameter1 = FloatField(validators=[DataRequired()])
   Parameter2 = FloatField(validators=[DataRequired()])
   Submit = SubmitField( Label = 'Calculate')

if __name__ == "__main__":
    app.run(debug = True)


    
