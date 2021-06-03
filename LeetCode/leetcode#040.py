class Solution:
    def combinationSum2(self, candidates, target):

        def dfs(candidates,target,start,end,path,res):

            if target < 0 :
                return
            if target == 0:
                res.append(path)
            
            
            for i in range(start,end):
                if i == start or i > start and candidates[i] != candidates[i - 1]:
                    if candidates[i] > target:
                        continue
                    dfs(candidates,target - candidates[i],i + 1,end,path + [candidates[i]],res)
        
        end = len(candidates)
        if end == 0:
            return []
        path = []
        res = []
        ans = []
        dfs(candidates,target,0,end,path,res)

        def remove_duplicate(arr):
            container = []
            ans = []
            for i in range(len(arr)):
                se = sorted(arr[i])
                if se not in container:
                    container.append(se)
                    ans.append(arr[i])
            return ans

        print('before remove duplicate:',res)
        ans = remove_duplicate(res)
        print('after remove duplicate:',ans)
        return ans


s = Solution()
s.combinationSum2([2,5,1,1,2,3,3,3,1,2,2],5)

        