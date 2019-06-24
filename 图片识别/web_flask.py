from flask import Flask,render_template,request,session,url_for
import sqlite3
import os
from db import db_search
from mian import base64_encode


#主网站
app = Flask(__name__)



@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/key',methods=['GET', 'POST'])
def key():
    msg4 = request.form['key']
    mag = db_search(msg4)
    q = len(mag)
    posts1 = []
    for i in range(q):
        msg1 = mag[i]
        g = str(base64_encode(msg1))
        f = g.lstrip('b')
        fll='data:image/jpg;base64,' + eval(f)
        posts1.append({'msg':fll})
        #if posts1==[]:
            #posts1.append({'error': '没有符合的图片'})
    #print (posts)
    return render_template('index.html',posts=posts1)

if __name__ == '__main__':
    app.run()
#host='10.66.31.234'