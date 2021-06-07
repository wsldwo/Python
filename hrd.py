print('数字华容道解法搜索程序 v1.0')
search_depth = [0,1,10,13,13,13,13,13,13,13,13,13]#13是个瓶颈，从14起就很慢了
min_step = 1000
solutions = []
n = int(input('请输入棋盘规模：'))
board = [[0] * n for i in range(n)]
print('请输入棋盘数据：')
for i in range(n):
    data = input(f'第{i + 1}行:')
    data_list = data.split()
    for j in range(n):
        board[i][j] = int(data_list[j])
print('初始棋盘如下：')
for i in range(n):
    print(board[i])

def check():
    if board[n - 1][n - 1] == 0:
        x = 1
        for i in range(n):
            for j in range(n):
                if board[i][j] == x:
                    x += 1
                elif i == n - 1 and j == n - 1:
                    return True
                else:
                    return False
                
    else:
        return False
'''
回溯法
x,y:空白坐标 其中，x为行，y为列
step:当前步数
path:移动轨迹
'''
def dfs(x,y,step,path):
    if step < search_depth[n]:
        if check():#找到可行解
            global min_step
            if step < min_step:#判断是否更优
                min_step = step
                solutions.append(path)
        else:
            #继续回溯
            #对于每一个空白，最多有四种操作

            #1、向左运动
            if y - 1 >= 0 and (len(path) == 0 or (x,y - 1) != path[-1][0]):#避免来回移动
                #交换数值
                board[x][y],board[x][y - 1] = board[x][y - 1],board[x][y]
                #回溯
                dfs(x,y - 1,step + 1,path + [(x,y),'-->',(x,y - 1)])
                #还原数值（因为回溯时并不是传递board副本）
                board[x][y],board[x][y - 1] = board[x][y - 1],board[x][y]

            #2、向右运动
            if y + 1 < n and (len(path) == 0 or (x,y + 1) != path[-1][0]):#避免来回移动
                #交换数值
                board[x][y],board[x][y + 1] = board[x][y + 1],board[x][y]
                #回溯
                dfs(x,y + 1,step + 1,path + [(x,y),'-->',(x,y + 1)])
                #还原数值（因为回溯时并不是传递board副本）
                board[x][y],board[x][y + 1] = board[x][y + 1],board[x][y]

            #3、向上运动
            if x - 1 >= 0 and (len(path) == 0 or (x - 1,y) != path[-1][0]):#避免来回移动
                #交换数值
                board[x][y],board[x - 1][y] = board[x - 1][y],board[x][y]
                #回溯
                dfs(x - 1,y,step + 1,path + [(x,y),'-->',(x - 1,y)])
                #还原数值（因为回溯时并不是传递board副本）
                board[x][y],board[x - 1][y] = board[x - 1][y],board[x][y]

            #4、向下运动
            if x + 1 < n and (len(path) == 0 or (x + 1,y) != path[-1][0]):#避免来回移动
                #交换数值
                board[x][y],board[x + 1][y] = board[x + 1][y],board[x][y]
                #回溯
                dfs(x + 1,y,step + 1,path + [(x,y),'-->',(x + 1,y)])
                #还原数值（因为回溯时并不是传递board副本）
                board[x][y],board[x + 1][y] = board[x + 1][y],board[x][y]

x = 0
y = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            x = i
            y = j
            break
dfs(x,y,0,[])
if len(solutions) > 0:
    print('已为您找到最优解：')
    #print(solutions[-1])
    for i in range(len(solutions[-1]) // 3):
        print(f'第{i + 1}步: {solutions[-1][i * 3:(i + 1) * 3]}')
else:
    print('很抱歉！未找到可行解！')

