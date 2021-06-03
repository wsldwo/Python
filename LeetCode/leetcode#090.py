class Solution:
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了38.20%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了11.67%的用户
    失败了一次，忘了加上去重措施2。。
    '''
    def subsetsWithDup(self, nums):
        # 组合函数
        def combine(nums,start,end,m,path,res):
            if m == 0:
                sort_path = sorted(path)
                if sort_path not in res: # 去重措施2
                    res.append(sort_path)
                return
            con = []
            for i in range(start,end + 1):
                if nums[i] not in con: # 去重措施1
                    combine(nums,i + 1,end,m - 1,path + [nums[i]],res)
                    con.append(nums[i])
        res = [[]]
        for i in range(1,len(nums) + 1):
            combine(nums,0,len(nums) - 1,i,[],res)
        print(res)
        return res
    '''
    评论区的思路：
    不需要编写组合函数，直接一边生成路径一边进行添加
    '''
    def subsetsWithDup2(self, nums):
        nums.sort() # 重要！！！先进行排序，方便回溯剪枝！！！
        len_nums = len(nums)
        res = [] # 结果集变量
        def dfs(start,path): # start 起始索引   path 中间结果，即每一个子集
            res.append(path) # 一边生成子集，一边添加到结果集
            for i in range(start,len_nums):
                if i > start and nums[i] == nums[i - 1]: # 去重剪枝
                    continue
                dfs(i + 1,path + [nums[i]])
        dfs(0,[])
        print(res)
        return res

        
s = Solution()
s.subsetsWithDup2([4,4,4,1,4])
#print([1,2,3]==[1,3,2])
