# 位置参数
# 计算a*b
def axb(a,b):
    if not isinstance(a,(int,float)):
        raise TypeError('not number!!!')
    if not isinstance(b,(int,float)):
        raise TypeError('not number!!!')
    return a*b
'''
a = input('a:')
a = int(a)
b = input('b:')
b = int(b)
print('%s * %s = %s' % (a,b,axb(a,b)))
'''
# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！ 
# 计算a的b次方
def power(a,b=2):
    if not isinstance(a,(int,float)):
        raise TypeError('not number!!!')
    if not isinstance(b,(int,float)):
        raise TypeError('not number!!!')
    if(a == 0 and b <= 0):
        return
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result
'''
a = input('a:')
a = int(a)
b = input('b:')
b = int(b)
print('%s的%s次方 = %s' % (a,b,power(a,b)))
print(power(10),power(5,4))
'''
# 可变参数
# 接收的是一个tuple
# 计算若干个数的平方和
def powerSum(*number):
    res = 0
    for x in number:
        res += x*x
    return res
'''
print(powerSum(1,3,5,7,9))
print(powerSum(6,7,8))
'''
# 关键字参数
# 接收的是一个dict
# 用户注册
def reg(name,age,**other):
    print('Name:',name,'Age:',age,'Other:',other,'has successfully registered!')
reg('Alice',18)
reg('Bob',25,Job='Gamer',City='Wuhan')
other = {'Job':'Teacher','Hobby':'Game','City':'Chibi'}
reg('Wsldwo',27,**other)

# 命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 用户注册
def reg2(name,age,*,job,city):
    print(name,age,job,city,'has successfully registered!')
reg2('Jackson',50,job='King of Pop',city='Heaven')

# 函数递归
# 计算阶乘 n!
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1) #引入了乘法表达式，不是尾递归
print(fact(3))

# 计算阶乘 n! 
# 尾递归优化
def fact2(n,res=1):
    if n == 1:
        return res
    return fact2(n-1,res*n) #仅返回递归函数本身，是尾递归
print(fact2(4))