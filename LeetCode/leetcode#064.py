class Solution:
    '''
    肯定是个动态规划题
    dp[i][j] 记录到达当前点最小路径值
    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

    执行结果：通过
    执行用时：56 ms, 在所有 Python3 提交中击败了61.85%的用户
    内存消耗：16.4 MB, 在所有 Python3 提交中击败了36.28%的用户
    '''
    def minPathSum(self, grid):
        m = len(grid) #行数
        n = len(grid[0]) #列数
        dp = [[0] * n for i in range(m)] #先列后行

        dp[0][0] = grid[0][0]
        #初始化第1行
        for i in range(1,n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        #初始化第1列
        for i in range(1,m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i - 1][j],dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
                    

