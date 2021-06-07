# 读文件

# 一般写法
try:
    f = open('file.txt','r',encoding='utf-8')  # reading 读模式  encoding='gbk', errors='ignore'
    print(f.read())
except BaseException as e:
    print(e)
finally:
    if f:
        f.close() #一定记得关闭

# 简略写法 （自动调用f.close()）
def openFiletxt():
    with open('file.txt','r',encoding='utf-8') as f:
        print(f.read())

# 读二进制文件
with open('zebra.jpg','rb') as f:
    print(f.read()[:10]) # 利用切片打印前一百个字符


# 写文件

# 一般写法
try:
    f = open('file.txt','w',encoding='utf-8') # writing 写模式 会覆盖之前的文件
    f.write('2020/4/16')
except Exception as e:
    print(e)
finally:
    if f:
        f.close()

# 简略写法
def writeFiletxt(s):
    with open('file.txt','a',encoding='utf-8') as f:# appending 追加模式
        f.write('\n') #换行
        f.write(s)
        

writeFiletxt('beautiful world')
writeFiletxt('beautiful world2')
writeFiletxt('beautiful world3')
openFiletxt()

# StringIO 
# 在内存中读写str
from io import StringIO
f = StringIO()
f.write('Today ')
f.write('is ')
f.write('Thursday!')
f.write('\n2020/4/16')
print(f.getvalue())

f = StringIO('Spike!\nJet!\nFye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip()) # strip()移除字符串头尾指定的字符（默认为空格或换行符）

# BytesIO
# 在内存中读写bytes
from io import BytesIO
f = BytesIO()
f.write('学习Python3.8'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe5\xad\xa6\xe4\xb9\xa0Python3.8')
print(f.read())

# 操作文件、目录
import os
import shutil

#print(os.path.abspath('.')) #打印当前绝对路径
if not os.path.isdir('testdir'): #判断当前目录是否存在某个文件夹
    os.mkdir('testdir') #在当前目录创建文件夹
#print(os.listdir()) #打印当前目录、文件
#os.rmdir('testdir') #在当前目录删除文件夹
#print(os.listdir())
#path = os.path.join(os.path.join(os.path.abspath('.'),'testdir'),'test.txt')
#print(path)
#if not os.path.isfile(path):
f = open(r'E:\Py Projects\testdir\test.txt','w',encoding='utf-8') #创建新文件    r前缀表示不使用转义
f.write('文件、目录操作\n')
f.write('2020/4/18\r')
f.close()
print(os.listdir('testdir'))

if os.path.isfile('E:\\Py Projects\\testdir\\test3.txt'):
    os.rename(r'testdir\test3.txt',r'testdir\test3.py') #文件重命名    r前缀表示不使用转义
print(os.listdir('testdir'))
if os.path.isfile('E:\\Py Projects\\test.txt'):
    os.remove('test.txt') #删除文件
print(os.listdir('testdir'))
shutil.copy('testdir\\test.txt','testdir\\test2.txt') #拷贝文件
print(os.listdir('.'))

def listfile(path,restrict=None): # 递归打印目录
    #print('path:',path)
    for x in os.listdir(path):
        filepath = os.path.join(path,x)
        if(restrict == None):
            if os.path.isfile(filepath): # 不能使用isfile(x)，而应该使用isfile(os.path.join(path,x)，因为x只包含文件名并不包括之前的路径
                print('file:',filepath)
            elif os.path.isdir(filepath): # 不能使用isdir(x)，而应该使用isdir(os.path.join(path,x)，因为x只包含文件名并不包括之前的路径
                print('directory:',filepath)
                listfile(filepath) # 不能使用listfile(x)，而应该使用listfile(os.path.join(path,x)，因为x只包含文件名并不包括之前的路径
        else:
            if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == restrict: 
                print('file:',filepath)
            elif os.path.isdir(filepath): 
                #print('directory:',os.path.join(path,x))
                listfile(filepath,restrict) 

#listfile('..\\')打印上一级目录
listfile('.') #打印全部文件
print('----------------')
listfile('.','.txt') #只打印txt文件

print('-------json 序列化---------')
# json 序列化
import json
# 把python对象转化为json对象
# 1、dict ===> json
dict1 = {'name':'Scarlet','age':20}
print(json.dumps(dict1))
#2、instance ===> json
class Player(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
player1 = Player('Kitana',22)
print(json.dumps(player1,default=lambda obj:obj.__dict__)) #通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量

# 把json对象转化为python对象
# 1、json ===> dict
json1 = '{"name": "Mileena", "age": 21}'
print(json.loads(json1))
# 2、json ===> instance
def dict2Player(d):
    return Player(d['name'],d['age'])
print(json.loads(json1,object_hook=dict2Player))

# 对中文进行JSON序列化
dict2 = {'name':'深刻反省','age':27}
print(json.dumps(dict2,ensure_ascii=True))
print(json.dumps(dict2))

print(json.dumps(dict2,ensure_ascii=False)) #正确转化


