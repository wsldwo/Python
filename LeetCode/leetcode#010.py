'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：

输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：

输入：s = "mississippi" p = "mis*is*p*."
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        sp = 0#s字串指针
        pp = 0#p字串指针
        while sp < len(s) and pp < len(p):
            if s[sp] == p[pp] or p[pp] == '.':
                sp +=1
                pp +=1
                continue
            else:

                if p[pp] == '*':
                    if pp > 0:
                        if s[sp] == p[pp-1] or p[pp-1] == '.':
                            sp+=1
                            continue
                        else:
                            pp+=1
                    else:
                        return False
                else:
                    pp+=1
        
        
        if pp == len(p) and sp < len(s):
            return False
        if sp < len(s):#没有匹配完
            return False
        if sp == len(s):
            if pp == len(p):#pattern没有多余的部分
                return True
            else:#pattern有多余的部分
                left_str = p[pp+1:]
                if len(left_str) % 2 == 0:
                    for x in left_str[-1::-2]:
                        if x != '*':
                            return False
                    return True
                else:
                    return False
s = Solution()
print(s.isMatch('aaa','aaaa'))