'''
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
'''
from queue import LifoQueue #栈

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 or not s:
            return False
        q = LifoQueue()
        for x in s:
            if x in ['(','[','{']:
                q.put_nowait(x)
            else:
                if q.empty():#特殊情况处理1
                    return False
                if x == ')':
                    if q.get_nowait() == '(':#使用get在栈容量为空时会进行等待导致超时
                        continue
                    else:
                        return False
                elif x == ']':
                    if q.get_nowait() == '[':#使用get在栈容量为空时会进行等待导致超时
                        continue
                    else:
                        return False
                elif x == '}':
                    if q.get_nowait() == '{':#使用get在栈容量为空时会进行等待导致超时
                        continue
                    else:
                        return False
        if q.qsize() > 0:#特殊情况处理2
            return False
        else:
            return True
s = Solution()
print(s.isValid('(({{{[['))
