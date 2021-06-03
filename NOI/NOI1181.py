'''
回溯法
'''
def dfs(in_stack,stack,out_stack):
    if len(in_stack) == 0 and len(stack) == 0:
        res.append(out_stack)
    else:
        if len(stack) > 0:
            dfs(in_stack,stack[:-1],out_stack + [stack[-1]])#出栈
        if len(in_stack) > 0:
            dfs(in_stack[1:],stack + [in_stack[0]],out_stack)#入栈
'''
递推公式法
'''
def cal(n):
    num = [1] * (n + 1)
    for i in range(2,n + 1):
        temp = 0
        for j in range(0,i):
            temp += num[j] * num[i - 1 - j]
        num[i] = temp
        print(f'f({i}):{num[i]}')

n = input('请输入参数n:')
'''
res = []#结果集变量
dfs([x for x in range(1,int(n) + 1)],[],[])
for index,value in enumerate(res):
    print(f'No.{index + 1}: {value}')
'''
cal(int(n))