class Solution:
    '''
    执行结果：通过
    执行用时：52 ms, 在所有 Python3 提交中击败了5.96%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了68.67%的用户
    '''
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        end = len(s) - 1
        #找到初始end位置
        while end >= 0 and s[end] == ' ':
            end -= 1
        #找到最后一个单词的前边
        while end >= 0 and s[end] != ' ':
            length += 1
            end -= 1
        return length
        
s = Solution()
print(s.lengthOfLastWord(' abc'))
        
        