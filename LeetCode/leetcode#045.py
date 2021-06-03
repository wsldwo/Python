class Solution:
    '''
    dfs depth first search 超时
    82 / 92 个通过测试用例
    '''
    def jump(self, nums):
        if not nums:
            return 0
        min_jump_count = [0]
        def dfs(nums,start,end,count,min_jump_count):
            #print(f'start:{start}  end:{end}')
            if start >= end:# 到达终点
                if count < min_jump_count[0] or min_jump_count[0] == 0:
                    min_jump_count[0] = count
                    #print(f'min_jump_count: {min_jump_count[0]}')
                return
            if count >= min_jump_count[0] and min_jump_count[0] != 0: # 优化2 
                return
            if nums[start] == 0:# 无法到达
                count = -1
                return

            if nums[start] >= end - start: # 优化1
                dfs(nums,end,end,count + 1,min_jump_count)
                return
            
            for i in range(1,nums[start] + 1):
                if nums[start + i] == 0 and start + i < end:
                    continue
                dfs(nums,start + i,end,count + 1,min_jump_count)

        dfs(nums,0,len(nums) - 1,0,min_jump_count)
        #print(min_jump_count[0])
        return min_jump_count[0]
    '''
    动态规划大法好！！！自己想出来的！！！牛逼！！！
    dp[i] 表示走到当前索引i位置所需要的最小跳跃次数
    dp [i] = min(dp[i-1],dp[i-2]......)
    '''
    def jump2(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(1,len(nums)):
            #计算dp[i]
            for j in range(i):
                if nums[j] < i - j:
                    #不可达
                    continue
                else:
                    #可达
                    if dp[j] < dp[i] or dp[i] == 0:
                        dp[i] = dp[j] + 1 #跳一步

        return dp[-1]

s = Solution()
print(s.jump2([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0]))