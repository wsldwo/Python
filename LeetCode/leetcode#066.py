class Solution:
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了33.42%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了56.36%的用户
    '''
    def plusOne(self, digits):
        length = len(digits)
        incre = 0 #进位
        for i in reversed(range(length)):
                if i == length - 1:
                    r = digits[i] + 1
                    if r >= 10:
                        incre = 1
                        digits[i] = 0
                        if i == 0:
                            #向前加一位
                            digits.insert(0,incre)
                    else:
                        incre = 0
                        digits[i] = r
                        break
                else:
                    if incre == 0:
                        break
                    r = digits[i] + incre
                    if r >= 10:
                        incre = 1
                        digits[i] = 0
                        if i == 0:
                            #向前加一位
                            digits.insert(0,incre)
                    else:
                        incre = 0
                        digits[i] = r
                        break
        print(digits)
        return digits


s = Solution()
s.plusOne([9,9])