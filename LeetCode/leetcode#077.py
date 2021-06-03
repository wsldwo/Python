class Solution:
    '''
    执行结果：通过
    执行用时：436 ms, 在所有 Python3 提交中击败了38.39%的用户
    内存消耗：16.1 MB, 在所有 Python3 提交中击败了78.19%的用户
    '''
    def combine(self, n: int, k: int):
        nums = list(range(1,n + 1)) #前闭后开
        def dfs(nums,start,end,count,k,path,res):
            if count == k:
                res.append(path)
                return
            for i in range(start,end + 1):
                dfs(nums,i + 1,end,count + 1,k,path + [nums[i]],res) #组合的诀窍是，只取后半截，把前半截全部砍掉，避免重复
        res = []
        dfs(nums,0,n - 1,0,k,[],res)
        #print(res)
        return res
        
s = Solution()
s.combine(7,5)