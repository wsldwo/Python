class Solution:
    '''
    超时算法！！！
    '''
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            if s[i] == ')':
                continue
            if maxlen > len(s) - i:
                break
            length = self.checkLength(s[i:],maxlen)
            if length > maxlen :
                maxlen = length
        return maxlen

    def checkLength(self,s: str,curlen) -> int:
        #print(s)
        maxlen = 0
        for i in range(curlen + 2,len(s) + 2,2):#额外加2，避免少读最后两个字符
            length = self.check(s[:i])
            if length > maxlen :
                maxlen = length

        return maxlen

    def check(self,s: str) -> int:
        #print(s)
        left = 0 #左括号数量
        for x in s:
            if x == '(':
                left += 1
            elif x == ')':
                left -= 1
            if left < 0:
                return -1
        if left == 0:
            return len(s)
        else:
            return -1

    #动态规划法
    '''
    我们定义 dp[i] 表示以下标i字符结尾的最长有效括号的长度。我们将 dp 数组全部初始化为 0。
    从前往后遍历字符串求解 dp 值。
    '''
    def longestValidParentheses2(self, s: str) -> int:
        maxlen = 0,lens = len(s)
        if lens == 0:return 0
        dp = [0] * lens
        for i in range(1,lens,1):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i > 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] > 2:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = dp[i - 1] + 2
        return max(dp)


s = Solution()
print(s.longestValidParentheses('(()()())()'))
#print('()()'[:6])

        