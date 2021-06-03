# 正则表达式 Regular Expression

# \d    匹配一个数字
# \w    匹配一个字母或数字
# \s    匹配一个空格
# .     匹配一个任意字符

# *     表示任意个字符（包括0个）
# +     表示至少一个字符
# ?     表示0个或1个字符
# {n}   表示n个字符
# {n,m} 表示n-m个字符

# ^     表示行的开头
# $     表示行的结尾

#进阶
#[]使用，表示范围
# [0-9a-zA-Z\_]   匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+  匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]* 匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19} 匹配由字母或下划线开头，后接0到19个数字、字母或者下划线组成的字符串

#()使用，表示分组
# r'^(\d{3})-(\d{3,8})$'  提取前后两段数字
# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串

# 匹配
import re
print(re.match(r'^\d{2,3}-\d{11}$','w90adj1d'))
print(re.match(r'^\d{2,3}-\d{11}$','86-19085298338'))

# 分组
exp1 = re.match(r'^(\w{4,6})(\d{4,6})@(\w{4,6})\.com$','wsldwo1994@python.com')
print(exp1)
print(exp1.group(0))
print(exp1.group(1))
print(exp1.group(2))
print(exp1.group(3))

# 切分
print('a b  c,d;j   g'.split(' ')) # 普通切分
print(re.split(r'[\s\,\;]+','a b  c,d;j   g')) # re切分

# datetime

from datetime import datetime
# 获取当前时间(本地)
now = datetime.now()
print(now)

# datetime ===> timestamp
# timestamp与时区毫无关系
day1 = datetime(2020,4,21,16)
print(day1)
print(day1.timestamp())

# timestamp ===> datetime
ts = 1587456000.0
print(datetime.fromtimestamp(ts))

# str ===> datetime
day2 = datetime.strptime('2020-6-1 18:0:0','%Y-%m-%d %H:%M:%S')
print(day2)

# datetime ===> str
day3 = datetime(2020,5,1,15,55)
print(day3.strftime('%A,%B;#%d %H:%M'))

# md5
# 摘要算法,又称哈希算法、散列算法.
# 通过一个函数,把任意长度的数据转换为一个长度固定的数据串,通常用16进制的字符串
# 目的是为了发现原始数据是否被人篡改过

import hashlib
md5 = hashlib.md5()
md5.update('a normal password'.encode('utf-8'))
print(md5.hexdigest()) # 生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示

# 用户注册&&登陆
user_db = {} #用户数据库
def caculate_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
def register(name,password):
    user_db[name] = caculate_md5(password) #存储用户密码的md5值
def login(name,password):
    if name in user_db.keys():
        if(user_db[name] == caculate_md5(password)):
            print('User %s login successfully!' % name)
        else:
            print('User %s login failed!' % name)
register('Alice','madgirl')
register('Bob','blackboy')
register('Chris','bowFighter')
print(user_db)
login('Chris','bowfighter')
login('Chris','bowFighter')

# md5 加盐
# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
def caculate_md5_v2(password):
    md5 = hashlib.md5()
    md5.update((password+'the-Salt').encode('utf-8'))
    return md5.hexdigest()
def register_v2(name,password):
    user_db[name] = caculate_md5_v2(password) #存储用户密码的"加盐"md5值
def login_v2(name,password):
    if name in user_db.keys():
        if(user_db[name] == caculate_md5_v2(password)):
            print('User %s login successfully!' % name)
        else:
            print('User %s login failed!' % name)

# hmac Keyed-Hashing for Message Authentication
# 带key的哈希(python自带的更为标准的“加盐”哈希)
import hmac
key = b'salt'
message = b'password'
hmac1 = hmac.new(key,message,digestmod='MD5') #传入的key和message都是bytes类型，str类型需要首先编码为bytes
print(hmac1.hexdigest())