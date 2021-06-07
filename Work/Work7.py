# 匿名函数
# 关键字lambda表示匿名函数，冒号前面表示函数参数，冒号后面的表达式结果为返回值
# 筛选奇数
print(list(filter(lambda x:x % 2 == 1,range(1,20))))

# 偏函数
# 固定住原函数的部分参数，从而在调用时更简单
import functools
int1 = functools.partial(int,base=2) # 二进制转化十进制
int2 = functools.partial(int,base=8) # 八进制转化十进制
int3 = functools.partial(int,base=16) # 十六进制转化十进制

print(int1('100110011110'))
print(int2('12707120637'))
print(int3('12873abcffe232'))

# 模块
# 在Python中，一个.py文件就称之为一个模块（Module）。
# 创建自己的模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
# 也可以有Python代码，因为__init__.py本身就是一个模块
# 例如 mycompany.web.www   mycompany.web.utils

# 导入模块
# import time

# 作用域

# public 成员：
# abc，x123，PI

# private 成员：（不应该被引用）
# _xxx和__xxx

# 特殊成员：（不应该被引用）
# __xxx__

# 安装第三方模块：
# pip install xxx

# 类和实例：
class Player(object):
    def __init__(self,name,gender,age): #__init__方法的第一个参数永远是self，表示创建的实例本身
        self.name = name
        self.gender = gender
        self.age = age
    def info(self): #在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
        print('%s %s %s' % (self.name,self.gender,self.age))
    def play(self):
        print('Player is playing...')

player1 = Player('PlayerA','Male',27)
player2 = Player('PlayerB','Female',25)
player1.info()
player2.info()

# 和静态语言不同，Python允许对实例变量绑定任何数据（动态添加任何属性）
player1.level = 18
print(player1.level)

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class PrivatePlayer(object):
    def __init__(self,name,gender,age):
        self.__name = name
        self.__gender = gender
        self.__age = age
    def getName(self):
        print(self.__name)
    def setName(self,name):
        self.__name = name

player3 = PrivatePlayer('Spike','Male',26)
player3.getName()
player3.setName('Valentine')
player3.getName()

# 继承与多态
class PlayerA(Player):
    def play(self): # 函数覆写
        print(self.name,'is playing A...')

player4 = PlayerA('Jack','Female',12)
player4.play()

# 获取对象信息
# 判断类型
# 1、使用type()函数
# 2、使用isinstance()函数
# 获取、修改，是否存在属性
# getattr()、setattr()以及hasattr()

# 实例属性 && 类属性
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
class Student(object):
    amount = 0 # 类属性
    def __init__(self,name,age):
        self.name = name # 实例属性
        self.age = age
        Student.amount += 1 # 类属性，自动加一

a = Student('Alice',16)
b = Student('Bob',18)
print(Student.amount)

# __slots__
# 限制实例能够绑定的属性
class Test(object):
    __slots__ = ('abc','efg') # 用tuple定义允许绑定的属性名称

t1 = Test()
t1.abc = 'abc' # 动态绑定属性
t1.efg = 'efg' # 动态绑定属性
# t1.hij = 156 报错

# @property
# 把一个方法变成属性调用
class Screen(object):
    @property #width.getter
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be a integer!')
        if value <= 0:
            raise ValueError('width must >= 0!')
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be a integer!')
        if value <= 0:
            raise ValueError('width must >= 0!')
        self.__height = value
    @property
    def resolution(self):
        #print('%s * %s =  %s' % (self.__width,self.__height,self.__width * self.__height ))
        return self.__width * self.__height

screen1 = Screen()
screen1.width = 1280
screen1.height = 720
print(screen1.resolution)

