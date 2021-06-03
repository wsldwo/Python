class Solution:
    '''
    动态规划题
    dp[i][j] 表示到达该点所有路径数
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 依题意，只能由上方和左侧的方格到达

    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了38.80%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了82.49%的用户
    之前有幸看到过题解！！
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)] #初始化dp数组，第一行、第一列的值均为1
        #计算dp数组
        for i in range(1,m):#行
            for j in range(1,n):#列
                #一行一行地计算
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

