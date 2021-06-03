class Solution:
    
    '''
    此算法超时
    '''
    def longestPalindrome(self, s):
        ls = len(s)
        maxstr = s[0]
        maxlen = 1
        i = 0#左指针
        j = 0#右指针
        for i in range(ls):
            for j in range(i+maxlen,ls):#range方法前闭后开
                '''
                如果当前子串的长度还没有已经检测到的最大回文串长度长，跳过！
                '''
                if maxlen >= (j+1-i):
                    continue
               
                if self.isPalindrome(s[i:j+1]) and len(s[i:j+1]) > maxlen:#切片操作前闭后开，s[i:j+1]才能表示索引i到索引j之间的字符串
                    maxstr = s[i:j+1]
                    maxlen = len(s[i:j+1])
        print(maxstr,maxlen)
        return maxstr
    
    def isPalindrome(self,s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    '''
    动态规划,还是超时，囧！！！
    '''
    def longestPalindrome2(self, s):
        l = len(s)
        dp = [[False] * l for x in range(l)] #创建储存状态的l*l方阵
        result = ''
        for i in range(l):#间距，长度为l+1
            for j in range(l):#起始位置
                k = j + i#结束位置
                if k >= l:#超出范围
                    break
                if i == 0:#长度为0
                    dp[j][k] = True
                elif i == 1:#长度为1
                    dp[j][k] = (s[j] == s[k])
                else:
                    dp[j][k] = dp[j+1][k-1] and (s[j] == s[k])
                if dp[j][k] and l + 1 > len(result):
                    result = s[j:k+1]
        print(result,len(result))
        return result
    '''
    中心扩展法
    '''
    def longestPalindrome3(self, s):
        start,end = 0,0
        for i in range(len(s)):
            left1,right1 = self.expand(s,i,i)
            left2,right2 = self.expand(s,i,i+1)
            if right1 - left1 > end - start:
                start,end = left1,right1
            if right2 - left2 > end - start:
                start,end = left2,right2
        return s[start:end+1]#切片，前闭后开

    def expand(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1,right -1







s = Solution()
print(s.longestPalindrome3('xyzawjdpcpdjwa'))#
#print('adjj'[0:100]) #切片超范围，不会报错！！！