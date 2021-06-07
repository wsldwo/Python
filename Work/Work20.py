# flask + MVC模式 + jinja2模板
# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。
# 在Jinja2模板中，用{% ... %}表示指令。很多时候，还需要循环、条件判断等指令语句，
# 除了Jinja2，常见的模板还有：
# Mako：用<% ... %>和${xxx}的一个模板；
# Cheetah：也是用<% ... %>和${xxx}的一个模板；
# Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。

from flask import Flask,request,render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html',time=datetime.now())

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    else:
        return render_template('form.html',message='Login Failed!',
        username=username)

if __name__ == '__main__':
    app.run()