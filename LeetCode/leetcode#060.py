class Solution:
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了31.81%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了38.69%的用户
    在草稿本上画出来的规律
    '''
    def getPermutation(self, n: int, k: int) -> str:
        def f(n):
            if n <= 1:
                return 1
            else:
                return n * f(n - 1)
        factorial = [1] * 10 #阶乘常数列表
        
        for i in range(1,10):
            factorial[i] = f(i)

        print(factorial)

        pos = [0] * n #位置记录，记录排列是第几档
        num = []
        for i in range(n):
            _sum = 0
            num.append(i + 1)
            for j in range(i):
                _sum += pos[j] * factorial[n - j - 1]
            pos[i] = (k - _sum) // factorial[n - i - 1]
            #pos[i] = (k - _sum) // f(n - i - 1)
        print(pos)
        
        last_not_zero_pos = 0
        res = ''
        for i in reversed(range(n)):
            if pos[i] != 0:
                last_not_zero_pos = i
                break
        for i in range(n):
            if i < last_not_zero_pos:
                res += str(num[pos[i]])
                num.remove(num[pos[i]])
            elif i == last_not_zero_pos:
                res += str(num[pos[i] - 1])
                num.remove(num[pos[i] - 1])
            else:
                res += str(num[-1])
                num.remove(num[-1])
                
        print(res)
        return res

s = Solution()
s.getPermutation(9,100)
'''
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

print(f(4))
'''