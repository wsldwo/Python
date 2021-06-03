# 切片
# 索引从0开始，末尾索引为-1
list1 = list(range(11)) #range返回一段从零开始前闭后开的整数序列 [0,11) 
print(list1)
#截取 第二个元素到末尾
print(list1[1:])
#截取 第二个元素到倒数第二个元素
print(list1[1:-1])
#截取 末尾5个数
print(list1[-5:])
#截取 间隔为3
print(list1[::3])

# 去除字符串首尾
# 字符串也是一种列表
def trim(str):
    start = 0
    end = -1
    while str[start] == ' ':
        start += 1
    while str[end] == ' ':
        end -= 1
    return str[start:end+1]
#print(trim('   a ssd c f          xyz v                         '))

# 迭代
'''
for x in 'awd ji':
    print(x)
for x,y in ((1,6),(7,-9),(-11,15)):
    print(x,y)
'''

# 找到数列中的最小最大值
def findMinAndMax(list):
    min = None
    max = None
    for x in list:
        if (min == None or max == None):
            min = x
            max = x
            continue
        if(x > max):
            max = x
        if(x < min):
            min = x
    return min,max

#print(findMinAndMax([90,-7,16,20,1000,-34,2,0]))

# 列表生成式 
# 只能用[]
# 1~10
print([x for x in range(1,11)])
# 奇数立方
print([x*x*x for x in range(1,11) if x % 2 == 1])
# 字母全组合
print([x+y for x in 'ABCD' for y in 'EFGH'])
# 小写字符串
print([x.lower()  for x in ['AjioBNKJm','oijNMJHlkz','JkopiUU',27,'156AWDJJjnJ'] if isinstance(x,str)])

# 生成器 generator
# 不断推算出后续的元素呢，这样就不必创建完整的list，从而节省大量的空间
# 生成器使用方式1：把一个列表生成式的[]改成()
for x in (y*y for y in range(11,21)):
    print(x)
# 生成器使用方式2：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def yanghuiTriangle(line):
    curL = 1 #当前行数，即当前行数字数量
    lastline = [1,1] #上一行列表
    curline = [] #当前行列表
    while curL<=line:
        if(curL == 1):
            print([1])
            
        elif(curL == 2):
            print([1,1])
            
        else:
            pos = 0
            curline = []
            while(pos<curL): #进行全1初始化
                curline.append(1)
                pos+=1

            #计算当前行内容
            pos = 1 #从第二个 到 倒数第二个
            while(pos<curL-1):
                curline[pos] = lastline[pos-1] + lastline[pos]
                pos+=1
            
            print(curline)
            lastline = curline #更新上一行列表
        
        curL += 1
        
#yanghuiTriangle(8)

# 把函数中的print函数全部替换成yield，可以得到一个生成器
def yanghuiTriangleGenerator(line):
    curL = 1 #当前行数，即当前行数字数量
    lastline = [1,1] #上一行列表
    curline = [] #当前行列表
    while curL<=line:
        if(curL == 1):
            yield([1])
            
        elif(curL == 2):
            yield([1,1])
            
        else:
            pos = 0
            curline = []
            while(pos<curL): #进行全1初始化
                curline.append(1)
                pos+=1

            #计算当前行内容
            pos = 1 #从第二个 到 倒数第二个
            while(pos<curL-1):
                curline[pos] = lastline[pos-1] + lastline[pos]
                pos+=1
            
            yield(curline)
            lastline = curline #更新上一行列表
        
        curL += 1

g = yanghuiTriangleGenerator(15)
for x in g: #遍历生成器
    print(x)

# 迭代器 
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#Python的for循环本质上就是通过不断调用next()函数实现的

it = iter([1,2,3,4,5])
while True:
    try:
        next(it)
    except StopIteration:
        break
    