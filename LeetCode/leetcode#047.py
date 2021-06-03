class Solution:
    '''
    有重复全排列的技巧是：1、每次需要把已使用元素给剔除掉 2、避免重复
    '''

    '''
    执行结果：通过
    执行用时：912 ms, 在所有 Python3 提交中击败了16.65%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了64.94%的用户
    这个not in 还是比较耗时间的，有没有更好的办法呢？
    '''

    def permuteUnique(self, nums):
        if not nums:
            return []
        
        def dfs(nums,path,res):#因为修改了遍历列表，所以不再使用start、end作为结束标志，path依然是中间结果，res为结果集
            if len(nums) == 1:
                if path + [nums[0]] not in res:#增加避免重复的条件，相比leetcode#046只需增加这一句
                    res.append(path + [nums[0]])
                return
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i + 1:],path + [nums[i]],res)
        
        res = []
        dfs(nums,[],res)
        print(res)
        return res
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了91.35%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了66.58%的用户
    看来还是在遍历过程中去重效率会更高！！！
    '''
    def permuteUnique2(self, nums):
        if not nums:
            return []
        
        def dfs(nums,path,res):#因为修改了遍历列表，所以不再使用start、end作为结束标志，path依然是中间结果，res为结果集
            if len(nums) == 1:
                res.append(path + [nums[0]])
                return
            container = []#测试重复的容器
            for i in range(len(nums)):
                if nums[i] not in container:#避免重复
                    container.append(nums[i])
                    dfs(nums[:i]+nums[i + 1:],path + [nums[i]],res)
        
        res = []
        dfs(nums,[],res)
        print(res)
        return res

s = Solution()
s.permuteUnique2([1,1,2])