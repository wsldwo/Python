from collections import defaultdict
class Solution:
    '''
    265 / 266 个通过测试用例
    超出时间限制
    最后执行的输入："kgfidhktkjhlk......"很长很长
    '''
    def minWindow(self, s: str, t: str) -> str:
        def check(a,b):
            for k in a.keys():
                if a[k] >= b[k]:
                    continue
                else:
                    return False
            return True
        len_s = len(s)
        len_t = len(t)
        alpha_dict = {}
        for i in range(len_t):
            if t[i] not in alpha_dict.keys():
                alpha_dict[t[i]] = 1
            else:
                alpha_dict[t[i]] += 1
        beta_dict = alpha_dict.copy()
        #print('alpha: ',alpha_dict.items(),' beta: ',beta_dict.items())
        min_length = 0
        res = ''
        for i in range(len_s):
            if len_s - i < len_t:
                break 
            if min_length == len_t:
                break
            for k in beta_dict.keys():
                beta_dict[k] = 0
            for j in range(i,len_s):
                if s[j] in beta_dict.keys():
                    beta_dict[s[j]] += 1
                #print('alpha: ',alpha_dict.values(),' beta: ',beta_dict.values())
                
                if check(beta_dict,alpha_dict):
                    if min_length == 0 or min_length > j - i + 1:
                        min_length = j - i + 1
                        res = s[i:j + 1] # 切片前闭后开
                    break
        print(res)
        return res
        '''
        滑动窗口，一个在字符串上滑动的窗口
        left,right分别为左、右指针
        '''

    def minWindow2(self, s: str, t: str) -> str:
        left,right = 0,0
        need = defaultdict(int) #可以计数的字典
        len_s = len(s)
        len_t = len(t)
        total = len_t #所需必须元素的总数量
        min_length = None
        res = ''
        for i in range(len_t):
            need[t[i]] += 1
        print(need)
        while len_s - left >= len_t:
            #右指针向右移动，直到满足需求
            while right < len_s and total > 0:
                if need[s[right]] > 0: #必须元素
                    total -= 1 
                need[s[right]] -= 1
                right += 1
            if total <= 0 and min_length > min_length == None  or (right - left + 1):
                min_length = right - left + 1
                res = s[left:right + 1] #切片 前闭后开
            #左指针向右移动，删除不必要部分
            while left < right and total <= 0:
                if need[s[left]] > 0: #必须元素
                    total += 1 
                need[s[left]] += 1
                left += 1
            if total == 0 and min_length > min_length == None  or (right - left + 1):
                min_length = right - left + 1
                res = s[left:right + 1] #切片 前闭后开
            need[s[left]] += 1
            left += 1
        print(res)
        return res
s = Solution()
s.minWindow2("aaaaaaaaaaaabbbbbcdd","abcdd")

