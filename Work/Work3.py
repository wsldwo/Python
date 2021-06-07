# 内置函数 
# 输出整数的16进制形式
str = input('Please input a integer:')
print(hex(int(str)))

import math
# 自定义函数
# 输入系数a、b、c 输出一元二次方程的解 
def method(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('Please input a number!!!')
    if not isinstance(b,(int,float)):
        raise TypeError('Please input a number!!!')
    if not isinstance(c,(int,float)):
        raise TypeError('Please input a number!!!')
    return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)


a = input('input a:')
a = int(a)
b = input('input b:')
b = int(b)
c = input('input c:')
c = int(c)

x1,x2 = method(a,b,c)
print('x1 = %s  x2 = %s' % (x1,x2))