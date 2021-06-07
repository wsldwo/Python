print('This is Visual Studio Code!')

#计算a+b,a-b
a = input('input number a :')
a = int(a)#强制类型转换
b = input('input number b :')
b = int(b)#强制类型转换
c = a + b
d = a - b
print('a + b = %d  a - b = %2d' % (c,d) )

#转义字符使用
print('I\'m learning Python 3.8') 

#不转义使用
print(r'默认\\不转义\\')

#多行打印
print('''多行测试
line1
line2
line3 ''')

a = 'ABC'
b = a
a = 'XYZ'
print('''a = 'ABC'
b = a
a = 'XYZ' ''')
print(b)

#计算成绩提升率
s1 = input('请输入上次成绩：')
s1 = int(s1)
s2 = input('请输入当前成绩：')
s2 = int(s2)
r = (s2-s1)*100/s1
print('成绩提升率：%.3f %%' % r)