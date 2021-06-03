class Solution:
    def spiralOrder(self, matrix):
        res = []
        '''
        初始坐标（i,j）
        '''
        if len(matrix) == 1:
            print(matrix[0])
            return matrix[0]
        '''
        修正：列的特殊情况处理
        '''
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            print(res)
            return res
        i,j = 0,0
        right_boundary = len(matrix[0]) - 1
        down_boundary = len(matrix) - 1
        left_boundary = 0
        up_boundary = 1
        while True:
            length1 = len(res)

            #向右
            while j < right_boundary and up_boundary <= len(matrix) - 1:#修正多打印的BUG
                res.append(matrix[i][j])
                j += 1
            right_boundary -= 1

            #向下
            while i < down_boundary and right_boundary >= 0:#修正多打印的BUG
                res.append(matrix[i][j])
                i += 1
            down_boundary -= 1

            #向左
            while j > left_boundary and down_boundary >= 0:#修正多打印的BUG
                res.append(matrix[i][j])
                j -= 1
            left_boundary += 1

            #向上
            while i > up_boundary and left_boundary <= len(matrix[0]) - 1:#修正多打印的BUG
                res.append(matrix[i][j])
                i -= 1
            up_boundary += 1

            length2 = len(res)
            if length1 == length2:
                if len(res) < len(matrix[0]) * len(matrix):
                    res.append(matrix[i][j]) #补完最后一个
                break
        
        while(len(res) > len(matrix[0]) * len(matrix)):#修正多打印的BUG
            res.pop()
        
        print(res)
        return res

s = Solution()
#s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
#s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
s.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

