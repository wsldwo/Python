class Solution:
    def countAndSay(self, n: int) -> str:

        def analyze(s:str):
            res = ''
            for i in range(len(s)):
                if i == 0:
                    res += s[i]
                    continue
                elif s[i] == s[i - 1]:
                    res += s[i]
                    continue
                else:
                    res += ','
                    res += s[i]
            #print(res)
            res_list = res.split(',')
            #print(res_list)
            ans = ''
            for i in range(len(res_list)):
                ans += str(len(res_list[i])) + res_list[i][0]
            #print(ans)
            return ans

        #analyze('3322251')

        if n == 1:
            return '1'
        if n == 2:
            return '11'
        if n == 3:
            return '21'
        
        if n > 3:
            ans = '21'
            for i in range(4,n + 1):
                ans = analyze(ans)
                #print(ans)
            return ans




s = Solution()
s.countAndSay(10)

                    
