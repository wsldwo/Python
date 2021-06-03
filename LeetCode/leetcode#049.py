class Solution:
    '''
    111 / 114 个通过测试用例
    超出时间限制
    '''
    def groupAnagrams(self, strs):
        res = [] # 结果集
        container = [] # 判重容器
        for i in range(len(strs)):
            temp1 = sorted(list(strs[i]))#原来是这里少加了)
            if temp1 not in container:#醉了，完全找不到错误！！
                container.append(temp1)
                r = []
                r.append(strs[i])
                for j in range(i + 1,len(strs)):
                    temp2 = sorted(list(strs[j]))
                    if temp2 == temp1:
                        r.append(strs[j])
                res.append(r) # 添加中间结果
        print(res)
        return res
    '''
    执行结果：通过
    执行用时：56 ms, 在所有 Python3 提交中击败了76.98%的用户
    内存消耗：17.6 MB, 在所有 Python3 提交中击败了61.69%的用户
    不得不说字典还是快啊！！！
    '''
    def groupAnagrams2(self, strs):
        res = {} # 结果集,改用字典
        for i in range(len(strs)):
            key = ''.join(sorted(list(strs[i])))
            if key not in res.keys():
                res[key] = [strs[i]]
            else:
                res[key].append(strs[i])
        return list(res.values())
    

s = Solution()
s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
        
        


