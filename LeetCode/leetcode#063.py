class Solution:
    '''
    动态规划题
    dp[i][j] 表示到达该点所有路径数
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 依题意，只能由上方和左侧的方格到达

    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了47.28%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.45%的用户
    '''
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid) # 行
        n = len(obstacleGrid[0]) # 列
        dp = [[0] * n for i in range(m)] # 先列后行

        #初始化第1行
        for i in range(n):
            if obstacleGrid[0][i] == 1: # 有石头
                dp[0][i] = -1 # 不可达
                for j in range(i + 1,n):
                    dp[0][j] = -1 # 后面的均不可达
                break
            else:
                dp[0][i] = 1
        #初始化第1列
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = -1
                for j in range(i + 1,m):
                    dp[j][0] = -1
                break
            else:
                dp[i][0] = 1
        #计算dp矩阵
        for i in range(1,m): # 行
            for j in range(1,n): # 列
                # 一行一行地计算
                if obstacleGrid[i][j] == 1: # 有石头
                    dp[i][j] = -1 # 不可达
                elif obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1: # 上方和左侧都有石头
                    dp[i][j] = -1 # 不可达
                else:
                    dp1,dp2 = 0,0
                    if dp[i - 1][j] != -1:
                        dp1 = dp[i - 1][j]
                    if dp[i][j - 1] != -1:
                        dp2 = dp[i][j - 1]
                    dp[i][j] = dp1 + dp2
        '''
        无语了，测试用例还真的在终点处放了一块石头！！！
        返回 -1 ，失败一次。
        '''
        if dp[m - 1][n - 1] <= 0:
            return 0
        return dp[m - 1][n - 1]
    '''
    简化版，去除-1状态，就用0表示不可到达
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了21.46%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了67.57%的用户
    '''
    def uniquePathsWithObstacles2(self, obstacleGrid) -> int:
        m = len(obstacleGrid) # 行
        n = len(obstacleGrid[0]) # 列
        dp = [[0] * n for i in range(m)] # 先列后行

        #初始化第1行
        for i in range(n):
            if obstacleGrid[0][i] == 1: # 有石头
                break
            else:
                dp[0][i] = 1
        #初始化第1列
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        #计算dp矩阵
        for i in range(1,m): # 行
            for j in range(1,n): # 列
                # 一行一行地计算
                if obstacleGrid[i][j] == 1 or obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1: # 有石头
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

                



