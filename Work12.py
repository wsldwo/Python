# itertools
# 无限迭代器
import itertools
# count() 数数
iter1 = itertools.count(2,4)#起始为2，间隔为4
'''
for x in iter1:
    print(x)
'''
# cycle() 循环
iter2 = itertools.cycle('terminator')
'''
for x in iter2:
    print(x)
'''
# repeat() 重复
iter3 = itertools.repeat('rev-9',10) #重复10次
for x in iter3:
    print(x)
# takewhile() 截取序列
print(list(itertools.takewhile(lambda x:  x < 100 ,iter1))) #只取小于100的部分
# chain() 把一组迭代对象串联起来，形成一个更大的迭代器
for x in itertools.chain('terminator','T-800'):
    print(x)
# groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('tterrrminnnnatttorr'):
    print(key,list(group))

# 上下文管理
# 只有实现了上下文管理才能使用with语句
# 方式1：通过__enter__和__exit__这两个方法实现

class Player(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __enter__(self):
        print('Player %s entered' % self.name)
        return self #此句不可少
    def __exit__(self,exc_type, exc_value, traceback):
        print('Player %s exited' % self.name)
    def play(self):
        print('Player %s is playing' % self.name)
    
with Player('Spike',26) as p1:
    p1.play()

# 方式2：通过@contextmanager
from contextlib import contextmanager

class Car(object):
    def __init__(self,name):
        self.name = name
    def drive(self,src,dst):
        print('%s is driving from %s to %s' % (self.name,src,dst))
@contextmanager
def get_a_car(name):
    print('###上文###')
    car1 = Car(name)
    yield car1
    print('###下文###')
with get_a_car('Nissan') as c1:
    c1.drive('陆水高中','赤马港')

# 通过@contextmanager，在某段代码执行前后自动执行特定代码
@contextmanager
def chat(name,no):
    print('%s entered chatroom #%s' % (name,no))
    yield
    print('%s left chatroom #%s' % (name,no))
with chat('Chris',101):
    print('chatting...')

# urllib

# get请求（参数放在链接中）
from urllib import request
# 方式1 直接打开链接
with request.urlopen('https://www.bd-film.cc/') as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data:',f.read().decode('utf-8')[:500])
# 方式2 打开一个request对象
# 此处模拟iphone访问网站
req1 = request.Request('https://www.ali213.net/')
req1.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req1) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('Data:',f.read().decode('utf-8')[:500])

# post请求（参数放在请求体中）
# 模拟登陆微博
from urllib import parse

print('Attempt login into weibo.cn...')
login_data = parse.urlencode([
    ('username', 'xtmexp'),
    ('password', 'xtmexp123456'),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req2 = request.Request('https://passport.weibo.cn/sso/login')
req2.add_header('Origin', 'https://passport.weibo.cn')
req2.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req2.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req2,data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# XML
# 操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 正常情况下，优先考虑SAX，因为DOM实在太占内存。
from xml.parsers.expat import ParserCreate

class MySaxHandler(object):
    def start_element(self,name,attrs):
        print('MySaxHandler:start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self, name):
        print('MySaxHandler:end_element: %s' % name)
    def char_data(self, text):
        print('MySaxHandler:char_data: %s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li attr1="attr"><a href="/python" arg="arg1">Python</a></li>
    <li><a href="/ruby" err="err2">Ruby</a></li>
</ol>
'''
handler = MySaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s> attrs:%s' % (tag,attrs))

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/> attrs:%s' % (tag,attrs))

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
parser = MyHTMLParser()
parser.feed('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>《孤岛惊魂3》也要重制了？封面反派配音演员泄露消息_游侠网 Ali213.net</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="keywords" content="孤岛惊魂3,重制,配音演员">
<meta  name="description" content="上周《孤岛危机》即将推出重制版的消息引发了网友们的热议，而因为当年的翻译使得另一位“孤岛兄弟”《孤岛惊魂》也有网友希望能推出重制。近日，《孤岛惊魂3》的反派配音演员Michael Mando似乎透露了本作将推出重制的消息。">

<link rel="alternate" media="only screen and (max-width:640px)" href="http://3g.ali213.net/news/html/504521.html" />

<link href="/news/css/news_2016.css" rel="stylesheet" type="text/css" />
<link href="//www.ali213.net/news/css/showbigpic_new.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="/news/js/UaJump.js"></script>
<script type="text/javascript" src="/news/js/jquery.min.js"></script>
</head>
<body>
<div id="append_parent"></div>
<div id="ajaxwaitid"></div>
</body>
</html>
''')


