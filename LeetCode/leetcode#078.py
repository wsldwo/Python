class Solution:
    '''
    执行结果：通过
    执行用时：36 ms, 在所有 Python3 提交中击败了84.90%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了62.73%的用户
    子集程序本质上是组合题，你需要把 Cn0 Cn1 .. Cnn 全部列举出来
    '''
    def subsets(self, nums):
        def dfs(nums,n,path,res):
            if n == 0:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:],n - 1,path + [nums[i]],res)
        res = [[]]
        for i in range(1,len(nums) + 1):
            dfs(nums,i,[],res)
        print(res)
        return res
s = Solution()
s.subsets([0,1,2,3])
