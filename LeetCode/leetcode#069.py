class Solution:
    '''
    暴力+1法
    执行结果：通过
    执行用时：2184 ms, 在所有 Python3 提交中击败了6.59%的用户
    内存消耗：14.5 MB, 在所有 Python3 提交中击败了99.48%的用户
    '''
    def mySqrt(self, x: int) -> int:
        n = x
        while True:
            if n * n > x:
                n //= 2
                if n * n < x and (n + 1) * (n + 1) > x:
                    return n
            elif n * n < x:
                if n * n < x and (n + 1) * (n + 1) > x:
                    return n
                n = n + 1
            else:
                return n
    
    '''
    二分法
    执行结果：通过
    执行用时：52 ms, 在所有 Python3 提交中击败了43.92%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.31%的用户
    '''
    def mySqrt2(self, x: int) -> int:
        def binarySearch(x,start,end):
            #print(f'binarySearch ###########  start:{start} end:{end}')
            if start >= end:
                #print(f'start >= end @@@@@ start:{start} end:{end}')
                return start 
            middle = (start + end) // 2
            if middle * middle > x:
                return binarySearch(x,start,middle - 1)
            elif middle * middle < x:
                if (middle + 1) * (middle + 1) > x:
                    return middle
                return binarySearch(x,middle + 1,end)
            else:
                return middle
        return binarySearch(x,0,x)

s = Solution()
print(s.mySqrt2(16))
