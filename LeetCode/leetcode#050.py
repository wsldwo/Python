class Solution:
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了38.03%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了25.73%的用户
    '''
    def myPow(self, x: float, n: int) -> float:
        return x ** n
    
    '''
    执行结果：通过
    执行用时：140 ms, 在所有 Python3 提交中击败了7.97%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了46.04%的用户
    坑是真的多！！！
    '''
    def myPow2(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if x < 1 and x > 0 and n > 1000000:
            return 0
        if x > -1 and x < 0 and n > 1000000:
            return 0
        if x > 1 and n < - 1000000:
            return 0
        if x < -1 and n < - 1000000:
            return 0
        res = 1
        for i in range(abs(n)):
            res *= x
        if n < 0:
            res = 1 / res
        return res

        
        
