class Solution:
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了55.97%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了30.64%的用户
    '''
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        #数据长度对齐
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a
        res = ''
        incre = 0
        for i in reversed(range(max(len_a,len_b))):
            r = int(a[i]) + int(b[i]) + incre
            print(r)
            if r == 3:
                res += '1'
                incre = 1
                if i == 0:#首位进一
                    res += '1'
            elif r == 2:
                res += '0'
                incre = 1
                if i == 0:#首位进一
                    res += '1'
            elif r == 1:
                res += '1'
                incre = 0
            else:# r == 0
                res += '0'
                incre = 0
        ans = ''.join(list(reversed(res)))
        print(ans)
        return ans
s = Solution()
s.addBinary('1010','1011')

