class Solution:
    '''
    动态规划：
    dp[i]：表示到达该点所需的最小跳跃次数
    dp[i] = min(dp[i-1],dp[i-2],...) + 1 (必须是可以一步到达)

    超出时间限制!!!!
    最后输入：[25000,24999,24998,24997,24996,24995,24994,24993,24992,24991,24990,.......]
    '''
    def canJump(self, nums):
        length = len(nums)
        if length == 1:
            return True
        if 0 not in nums:
            return True
        if nums[0] >= length - 1:
            return True
        dp = [-1] * length # 初始化 dp数组

        for i in range(length):
            if i == 0 and nums[i] > 0:
                dp[i] = 0
            else:
                for j in range(i):
                    if nums[j] >= i - j and dp[j] != -1:#可以一步到达
                        if dp[i] == -1 or dp[j] + 1 <  dp[i]:
                            dp[i] = dp[j] + 1

                if dp[i] > 0 and nums[i] >= length - 1 - i:
                    return True
        
        if dp[-1] == -1:
            return False
        else:
            return True
    
    '''
    贪心法
    实时维护 最远可以到达的位置，如果 最远可以到达的位置 大于等于数组中的最后一个位置，那就说明最后一个位置可达
    '''
    def canJump2(self, nums):
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost: # 可达
                rightmost = max(rightmost, i + nums[i]) # 更新最远可达距离
                if rightmost >= n - 1:
                    return True
        return False


s = Solution()
print(s.canJump2([2,0,0]))
