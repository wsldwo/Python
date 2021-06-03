class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        matrix_copy = [[0] * length for i in range(length)]

        for i in range(length):
            k = 0
            for j in reversed(range(length)):
                matrix_copy[i][k] = matrix[j][i]
                k += 1
        #拷贝数组
        for i in range(length):
            for j in range(length):
                matrix[i][j] = matrix_copy[i][j]


        print(matrix)

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
