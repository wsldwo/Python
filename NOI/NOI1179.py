'''
students: 待分配的学生列表
books:待分配的书籍列表
path:中间结果
res:结果集
'''
def dfs(students,books,path):
    if len(students) == 0:
        res.append(path)
    else:
        #每次只解决第一个学生的分书需求
        for i in range(len(books)):
            if(books[i] != students[0]):#默认初始状态：i号学生拿i号书
                dfs(students[1:],books[:i] + books[i + 1:],path + ['book' + str(books[i]),'-->','student' + str(students[0])])

n = input()
res = []
dfs(list(range(1,int(n) + 1)),list(range(1,int(n) + 1)),[])
for k,v in enumerate(res):
    print('No.',k + 1,': ',v)

