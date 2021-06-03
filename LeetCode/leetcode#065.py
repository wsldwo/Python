import re
class Solution:
    '''
    NICE!一次通过！！！
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了51.85%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了33.89%的用户
    re模块牛逼！
    '''
    def isNumber(self, s: str) -> bool:
        '''
        pattern 编写练习
        小数点 应该用 \. 而不是 .
        适当使用()进行分组的好处是：1、表达式看起来清晰 2、限制 * + ？作用域
        '''
        matchobject = re.match(r'^([+-]?)([0-9]+|[0-9]+\.|[0-9]+\.[0-9]+|\.[0-9]+)(|[eE][+-]?[0-9]+)$',s)
        if matchobject:
            print('match:',matchobject.groups())
            return True
        else:
            print('not match')
            return False
s = Solution()
s.isNumber('+1001e011')