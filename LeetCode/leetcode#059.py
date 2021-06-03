class Solution:
    '''
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了63.88%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.24%的用户
    '''
    def generateMatrix(self, n):
        matrix = [[0] * n for i in range(n)]
        i,j = 0,0
        val = 1
        right_boundary = n - 1
        down_boundary = n - 1
        left_boundary = 0
        up_boundary = 1
        while val < n * n:
            #向右
            while j < right_boundary:
                matrix[i][j] = val
                val += 1
                j += 1
            right_boundary -= 1

            #向下
            while i < down_boundary:
                matrix[i][j] = val
                val += 1
                i += 1
            down_boundary -= 1

            #向左
            while j > left_boundary:
                matrix[i][j] = val
                val += 1
                j -= 1
            left_boundary += 1

            #向上
            while i > up_boundary:
                matrix[i][j] = val
                val += 1
                i -= 1
            up_boundary += 1
        #补上最后一个
        matrix[i][j] = val
        print(matrix)
        return matrix
s = Solution()
s.generateMatrix(1)
