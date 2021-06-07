'''
本程序文件主要使用回溯法、动态规划法，对“n球 r盒”问题进行求解
问题规模：1 <= r <= n <= 20
问题3：n个不同球 放入r个相同盒子 不允许空盒
'''
import copy,string,random
n = int(input('n:'))
r = int(input('r:'))
boxes = [[] for i in range(r)]#二维数组的正确初始化
res = []
no = 0
'''
回溯法
'''
def dfs(ball_id:int):
    if ball_id <= n:
        for i in range(r):
            boxes[i].append(ball_id)#把i号球放入盒中
            dfs(ball_id + 1)#进行下一轮回溯
            boxes[i].pop()#把i号球取出，避免影响其它路线
    else:
        for box in boxes:
            if len(box) == 0:#不允许空盒子
                return
        sorted_boxes = copy.deepcopy(sorted(boxes,key=lambda x:x[0]))#在三维列表中添加二维列表必须使用深拷贝，否则不生效！！！
        if sorted_boxes not in res:#排序去重，没办法了，剪枝又不会剪，只有去重才能维持生活这样子
            res.append(sorted_boxes)
            global no
            no += 1
            print(f'方案{no}: {sorted_boxes}')

'''
动态规划法
dp[i][j] = dp[i - 1][j] * j + dp[i - 1][j - 1]
'''
def cal(n:int,r:int):
    dp = [[0] * (r + 1) for i in range(n + 1)]#列在前 行在后
    for i in range(1,n + 1):
        for j in range(1,r + 1):
            if j == 1:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] * j + dp[i - 1][j - 1]
    return dp[n][r]
#dfs(1)
#print(f'cal:{cal(n,r)}')

'''
回溯法2，昨晚用c写失败了，今天调休一天，在家用python试试
终于成功了，太不容易了------2021年5月24日 17：24：54
先等等，好像还有问题。。
n = 4 r = 3  答案少了 1 2 3 1
大概是搞定了，居然还有遗失路线------2021年5月24日 18：42：30
'''
balls = [0] * (n + 1)
balls[0] = -1#此位置不使用
solu = 0
def dfs2(heap_id:int,start:int,end:int):
    #print(f'just enter ### balls:{balls},start:{start},end:{end},heap_id:{heap_id}')
    if balls.count(0) == 0:
        for i in range(1,r + 1):
            if i not in balls:
                return
        for i in range(1,n + 1):
            if balls[i] > r:
                return

        global solu
        solu += 1
        print(f'solu{solu}:{balls}')
    elif start < end:
        leader = -1
        if heap_id not in balls:
            for i in range(start,end):
                if balls[i] == 0:
                    leader = i
                    balls[i] = heap_id#找到堆头元素
                    if balls.count(0) == 0:
                        dfs2(heap_id,n + 1,end)
                        balls[i] = 0
                        return
                    break
        
        x = balls[start:end].count(0)

        for i in range(start,end):
            if balls[i] == 0:
                #路线1，进堆
                balls[i] = heap_id
                dfs2(heap_id,i + 1,end)
                balls[i] = 0
                #路线2，不进堆
                dfs2(heap_id,i + 1,end)

                break#解决重复路线，一次只处理一个节点
        '''
        遗失路线
        '''
        if x == 0:
            for i in range(1,start):
                if balls[i] == 0:
                    #路线1，进堆
                    balls[i] = heap_id + 1
                    dfs2(heap_id + 1,i + 1,end)
                    balls[i] = 0
                    #路线2，不进堆
                    #dfs2(heap_id,i + 1,end)

                    break#解决重复路线，一次只处理一个节点
        
        '''
        这里是我没想到的，堆头元素居然也要进行回退，避免影响其他路线
        看来回溯法里面的，数据回退真的是要小心小心再小心
        '''
        if leader != -1:
            balls[leader] = 0 #必须还原，否则影响其他路线

    elif start >= end:
        if heap_id + 1 <= r:
            pos = balls.index(0)
            dfs2(heap_id + 1,pos,end)
dfs2(1,1,n + 1)
print(f'cal:{cal(n,r)}')