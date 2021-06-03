class Solution:
    def combinationSum(self, candidates, target):
        def dfs(candidates,target,start,length,path,res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start,length):#神奇的depth first search，神奇的去重
                dfs(candidates,target - candidates[i],i,length,path + [candidates[i]],res)
        
        length = len(candidates)
        if length == 0:
            return []
        path = []
        res = []
        dfs(candidates,target,0,length,path,res)
        print(res)
        return res

s = Solution()
s.combinationSum([2,3,5],8)