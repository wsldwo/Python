class Solution:
    '''
    一次通过，NICE!!!
    无重复全排列的技巧是每次需要把已使用元素给剔除掉
    '''
    def permute(self, nums):
        if not nums:
            return []
        
        def dfs(nums,path,res):#因为修改了遍历列表，所以不再使用start、end作为结束标志，path依然是中间结果，res为结果集
            if len(nums) == 1:
                res.append(path + [nums[0]])
                return
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i + 1:],path + [nums[i]],res)
        
        res = []
        dfs(nums,[],res)
        print(res)
        return res

s = Solution()
s.permute([1])

