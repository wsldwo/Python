# Python3.x中的字符串有两种：str和bytes
# str   文本字符串
# bytes 字节字符串 （一般来自网络读取的数据、从二进制文件（图片等）中读取的数据）
# 互相转化
# str.encode('某编码方式') -> bytes
# bytes.decode('某编码方式') -> str

a = 'python3.8' # Python3.x 字符串默认Unicode编码，通常一个字符占用2个字节
print(type(a))
print(len(a))
print('a:',a)

b = b'python3.8' # Ascii编码,不能包含中文   bytes can only contain ASCII literal characters.
print(type(b))
print(len(b))
print('b:',b)

c = 'python3.8'.encode('ascii') # Ascii编码,不能包含中文，一个字符占用1个字节
print(type(c))
print(len(c))
print('c:',c)

d = '学习python3.8' # Python3.x 字符串默认Unicode编码
print(type(d))
print(len(d))
print('d:',d)

e = '学习python3.8'.encode('utf-8')
print(type(e))
print(len(e))
print('e:',e)


print('a==b',a==b)
print('b==c',b==c)
print('d==e',d==e)

# 邮件收发原理
# MUA Mail User Agent 邮件用户代理      比如，用户使用的各种邮箱软件
# MTA Mail Transfer Agent 邮件传输代理  比如，邮件服务提供商，网易、新浪
# MDA Mail Delivery Agent 邮件投递代理  比如，对方电子邮箱对应的服务器
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

print('\r\n')
print('######sqlite3 使用@@@@@@')
# sqlite3 使用
# 占位符使用？
import sqlite3
# 初始化数据库
'''
conn = sqlite3.connect('player.db')
cursor = conn.cursor()

cursor.execute('create table player (id varchar(20) primary key,name varchar(20),age int)')  #不能重复建表
cursor.execute('insert into player (id,name,age) values (\'P-001\',\'Spike\',26)')  #不能重复插入
cursor.execute('insert into player (id,name,age) values (\'P-002\',\'Fye\',20)')
cursor.execute('insert into player (id,name,age) values (\'P-003\',\'Jet\',36)')
cursor.execute('insert into player (id,name,age) values (\'P-004\',\'Ain\',14)')

cursor.close()
# 提交事务
conn.commit()
conn.close()
'''
conn = sqlite3.connect('player.db')
cursor = conn.cursor()

cursor.execute('insert into player (id,name,age) values (\'P-005\',\'whatever\',28)') #插入 id = P-005 玩家
cursor.execute('select * from player') # 查询所有玩家
# fetchall()方法获取结果集中所有条目
print(cursor.fetchall())

cursor.execute('select * from player where age > ? and age <= ?',(15,28)) # 查询年龄大于15小于等于28的玩家
print(cursor.fetchall())

cursor.execute('update player set age = ? where id = ?',(12,'P-004')) # 修改 Ain年龄
cursor.execute('select * from player') 
print(cursor.fetchall())

cursor.execute('delete from player where id = ?',('P-005',)) # 删除 id = P-005 玩家
cursor.execute('select * from player') 
print(cursor.fetchall())


cursor.close()
# 提交事务
conn.commit()
conn.close()

# MySQL 使用
# 占位符使用%s
import mysql.connector
conn = mysql.connector.connect(user='wsldwo', password='2020427',database='db1') # root账户 user='root', password='Complex2020'
cursor = conn.cursor()
'''
cursor.execute('create table player (id varchar(20) primary key,name varchar(20),age int)') #不能重复建表
cursor.execute('insert into player (id,name,age) values (%s,%s,%s)',('G-001','Lelouch',19)) #不能重复插入
cursor.execute('insert into player (id,name,age) values (%s,%s,%s)',('G-002','C.C.',500))
cursor.execute('insert into player (id,name,age) values (%s,%s,%s)',('G-003','Suzaku',19))
cursor.execute('insert into player (id,name,age) values (%s,%s,%s)',('G-004','Kallen',18))
'''

cursor.execute('select * from player where age >= %s',(19,)) # 查询年龄大于等于19的所有玩家
# fetchall()方法获取结果集中所有条目
print(cursor.fetchall())

cursor.execute('update player set age = %s where id = %s',(23,'G-002')) #修改C.C.年龄
cursor.execute('select * from player') 
print(cursor.fetchall())

cursor.execute('insert into player (id,name,age) values (%s,%s,%s)',('G-005','Charles',50)) #增加Charles
cursor.execute('select * from player') 
print(cursor.fetchall())

cursor.execute('delete from player where id = %s',('G-005',)) # 删除Charles
cursor.execute('select * from player') 
print(cursor.fetchall())


cursor.close()
# 提交事务
conn.commit()
conn.close()

# SQLAlchemy 使用
# 传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换

from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类
Base = declarative_base()
# 定义Player对象
class Player(Base):
    __tablename__ = 'player'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    age = Column(Integer)

engine = create_engine('mysql+mysqlconnector://wsldwo:2020427@localhost:3306/db1')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()
#new_player = Player(id='G-006',name='Sherly',age=19) 
#session.add(new_player) #不能重复插入

#new_player = Player(id='G-007',name='Orange',age=33) 
#session.add(new_player) #不能重复插入

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
playerlist = session.query(Player).filter(Player.age>20).all()

for x in playerlist:
    print(x.id,x.name,x.age)

# 提交即保存到数据库
session.commit()
# 关闭session
session.close()