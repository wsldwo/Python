class Solution:
    '''
    执行结果：通过
    执行用时：32 ms, 在所有 Python3 提交中击败了99.88%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了76.67%的用户
    '''
    def setZeroes(self, matrix):
        m = len(matrix) #行
        n = len(matrix[0]) #列
        set_zero_row = set()
        set_zero_col = set()
        for i in range(m):
            if len(set_zero_row) == m or len(set_zero_col) == n:#一点点优化
                break
            for j in range(n):
                if matrix[i][j] == 0:
                    set_zero_row.add(i)
                    set_zero_col.add(j)
        for i in set_zero_row:
            for j in range(n):
                matrix[i][j] = 0
        for i in set_zero_col:
            for j in range(m):
                matrix[j][i] = 0

