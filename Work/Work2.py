# list 内置有序列表
list1 = ['abc',78,True,'xyz']
list1.insert(2,'spike') # 总是在前面插入
list1.insert(-1,'fye')
list1.append('ain') # 队尾加入
list1.pop() # 删除队尾
print(list1)

# tuple 内置有序列表 不可改
tuple1 = ('def',False,33,-7.21)
print(tuple1)

# for in 循环
for x in ['Darwin','Sherry','Chris']:
    print('Hello',x,'!')

# while 循环
sum = 0
a = 1
while a<10:
    sum += a
    a += 2
print(sum) 

# dict 字典 类似java中的Map,储存key-value
score = {'Leon':89,'Sheeva':83,'Wisker':78}
for stu in score:
    print(stu,score[stu])

# set 集合 只存储key，内部元素无序、不重复
set1 = set([1,4,8,11]) #创建一个set，需要提供一个list作为输入集合
set1.add('six')
set1.add(9)
print(set1)