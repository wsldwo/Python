class Solution:
    '''
    动态规划
    '''
    def maxSubArray(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        dp = [0] * length#存储以当前节点结尾的最大子序和
        for i in range(length):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(nums[i],dp[i - 1] + nums[i])
        return max(dp)
            

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))