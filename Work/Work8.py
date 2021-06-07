# 多重继承
# 通过多重继承可以组合多个类的功能
class A(object):
    def drive(self):
        print('driving...')
class B(object):
    def drift(self):
        print('drifting...')
class C(A,B):
    pass
    
c = C()
c.drive()
c.drift()

# 枚举类
from enum import Enum
class Gender(Enum):
    Female = 0
    Male = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
stu1 = Student('Alice',Gender.Female)
print(stu1.gender == Gender.Female)

# type()
# 通过type()函数动态创建一个类
#要创建一个class对象，type()函数依次传入3个参数：
#1、class的名称；
#2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3、class的方法名称与函数绑定

def play(self,arg):
    print('play %s' % arg)

Player = type('Player',(object,),dict(work=play)) # 创建Player类
player1 = Player()
player1.work('Dead or Alive')

# 错误处理
# try...except...finally...

try:
    print('try:')
    #print(2/0)
except BaseException as e:  # 捕获异常
    print('except:',e)
    raise ValueError('can not divided by 0!') # 抛出异常
finally:
    print('finally:')

# 调试

# 方式1：print() 打印

# 方式2：assert  断言
# 断言的开关“-O”是英文大写字母O，不是数字0
# 如果断言失败，assert语句本身就会抛出AssertionError
# python -O err.py

def divide(a,b):
    assert b != 0,'b == 0'
    return a/b
#print(divide(3,0))

# 方式3：logging
# Log等级：debug，info，warning，error
# 指定level=INFO时，logging.debug就不起作用了
# 指定level=WARNING后，debug和info就不起作用了
import logging
logging.basicConfig(level=logging.INFO) # 设定log等级
a = 7
b = 3
logging.info('b = %s' % b)
#print(a/b)

# 方式4：pdb.set_trace() 设置断点

# 单元测试
# 用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
# 为了编写单元测试，需要引入Python自带的unittest模块，从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
# 例如：可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
def myAbs(n):
    if n >= 0 :
        return n
    else :
        return -n

import unittest
class TestMyAbs(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(3,myAbs(3))
    def test_negetive(self):
        self.assertEqual(5,myAbs(-5))
    def test_0(self):
        self.assertEqual(0,myAbs(0))
    def test_typeerror(self):
        with self.assertRaises(TypeError):
            myAbs('awd')
    
    def setUp(self): #完成准备工作
        print('setUp...')
    def tearDown(self): #恢复现场
        print('tearDown...')
    

# 运行单元测试
if __name__ == '__main__':
    unittest.main()

# 文档测试
# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
# 严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段烦人的输出
class Student2(object):
    '''
    >>> stu = Student2('Spike',91)
    >>> stu.getName()
    'Spike'
    >>> stu.getGrade()
    91
    '''
    def __init__(self,name,grade):
        self.__name = name
        self.__grade = grade

    def getName(self):
        return self.__name
    
    def getGrade(self):
        return self.__grade


# 运行文档测试 (不能与单元测试同时运行)
if __name__=='__main__':
    import doctest
    doctest.testmod() # 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
