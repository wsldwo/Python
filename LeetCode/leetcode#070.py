class Solution:
    #'这题又是一个动态规划题'
    #'每次只能跨一步或者两步'
    '''
    dp[i] 表示到达第 i + 1 层台阶的方案数
    dp[i] = dp[i - 1] + dp[i - 2]

    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了29.98%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了20.83%的用户
    '''
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1 #到达第一层
        if n > 1:
            dp[1] = 2 #到达第二层
        for i in range(2,n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1] #到达第n层