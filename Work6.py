# 高阶函数
# 函数名也是变量
# 所以，一个函数可以接收另一个函数作为参数
def square (x):
    return x*x

def squareAdd (f,*x):#可变参数需要放在后方，编译才可通过
    sum = 0
    for n in x:
        sum += f(n)
    return sum

print(squareAdd(square,1,3,5,7))

# map && reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# reduce()函数接收两个参数，一个是函数，一个是Iterable，reduce把结果继续和序列的下一个元素做累积计算 
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 规范首字母大写，其余小写
def normalize(s):
    res = ''
    pos = 0
    while pos < len(s):
        if pos == 0:
            res += s[pos].upper() #字符衔接使用+=
        else :
            res += s[pos].lower()
        pos += 1
    return res

print(list(map(normalize,['aLiCe','DARwiN','pAtrIck','JamES']))) #Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

# 字符串转浮点数
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]
def f(x,y):
    return x * 10 + y
def handle(s):
    ns = ''
    pot = 1
    pos = 0
    count = False
    while(pos < len(s)):
        if count:
            pot *= 10 #要除的倍数
        if s[pos] == '.':
            count = True
        else:
            ns += s[pos] #剔除小数点
        pos += 1
    return pot,ns

#print(reduce(f,map(char2num,'89127.152')))

pot,ns = handle('89127.152')
print(reduce(f,map(char2num,ns))/pot)

# filter
# 接收一个函数和一个序列，根据返回值是True还是False决定保留还是丢弃该元素
# 筛选回数 12321，909
def seq(): #返回一个从11开始的无限的整数序列
    n = 10
    while True:
        n += 1
        yield n
def isMirror(n):
    s = str(n)
    pos = 0
    posR = len(s)-1
    while (pos<posR):
        if s[pos] == s[posR]:
            pos += 1
            posR -= 1
        else :
            return False
    return True
def MirrorNum(): 
    seq1 = filter(isMirror,seq())
    while True:
        n = next(seq1)
        yield n

list1 = []
for n in MirrorNum(): #函数（生成器）也能用于for循环
    if n<1000:
        list1.append(n)
    else:
        print(list1)
        break

# sorted
# 接收一个序列和一个key
# 根据成绩排序
def byScore(t):
    return t[1]
# 根据姓名排序
def byName(t):
    return t[0]
stu = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(stu,key=byScore,reverse=True))
print(sorted(stu,key=byName))

# 返回函数
# 计时器实现，每次调用计时数加一
n = 0
def Counter():
    n = [0] # n = 0 行不通，必须使用列表
    def count():
        n[0] += 1
        return n[0]
    return count

count1 = Counter()
print(count1(),count1(),count1(),count1(),count1(),count1(),)
