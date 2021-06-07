# flask 使用
# 一个比较流行的Web框架
from flask import Flask
from flask import request

app = Flask(__name__)

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
@app.route('/signin',methods=['GET'])
def signin():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin',methods=['POST'])
def login():
    if request.form['username']=='wsldwo' and request.form['password']=='2020427':
        return '<h3>Hello,wsldwo!</h3>'
    else:
        return '<h3>Login failed!</h3>'

if __name__ == '__main__':
    app.run()

# Flask自带的Server在端口5000上监听
# 输入首页地址http://localhost:5000/
# 再在浏览器地址栏输入http://localhost:5000/signin，会显示登录表单

#除了Flask，常见的Python Web框架还有：
#   Django：全能型Web框架；
#   web.py：一个小巧的Web框架；
#   Bottle：和Flask类似的Web框架；
#  Tornado：Facebook的开源异步Web框架。
