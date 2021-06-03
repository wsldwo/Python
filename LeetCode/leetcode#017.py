'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    
    def letterCombinations(self, digits):
        if digits == '':#修正特殊情况，力扣的极端情况好恶心
            return []

        num_dict = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        seq = []
        for x in digits:
            seq.append(num_dict[int(x)])
        print(seq)#['def', 'ghi']
        return self.f(seq)
    
    def f(self,seq,res=''):#res 中间结果
        if len(seq) == 0:#长度为0，递归的终点
            return [res]
        result = []#result 结果集
        for x in seq[0]:
            r = self.f(seq[1:],res+x)#r 临时变量
            if r != None:
                result.extend(r)
        return result
            
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def backtrack(conbination,nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter,nextdigit[1:])

        res = []
        backtrack('',digits)
        return res

作者：z1m
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


s = Solution()
print(s.letterCombinations('325'))