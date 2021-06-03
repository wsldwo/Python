class Solution:
    '''
    执行用时：56 ms, 在所有 Python3 提交中击败了42.64%的用户
    内存消耗：14.7 MB, 在所有 Python3 提交中击败了94.70%的用户

    牛逼，一次通过！
    '''
    def isValidSudoku(self, board):

        def check(line):
            container = []
            for i in range(len(line)):
                if line[i] == '.':
                    continue
                elif line[i] not in container:
                    container.append(line[i])
                else:
                    return False
            return True
        
        for i in range(9):
            if not check(board[i]):#检测每行
                return False
        
        for i in range(9):
            if not check([board[j][i] for j in range(9)]):#列表生成式，检测每列
                return False
        
        def matrix(a,b):#根据左上角，返回3x3矩阵数据
            li = []
            for i in range(a,a + 3):
                for j in range(b,b + 3):
                    li.append(board[i][j])
            return li
        
        if not check(matrix(0,0)):
            return False
        
        if not check(matrix(0,3)):
            return False
        
        if not check(matrix(0,6)):
            return False
        
        if not check(matrix(3,0)):
            return False
        
        if not check(matrix(3,3)):
            return False
        
        if not check(matrix(3,6)):
            return False
        
        if not check(matrix(6,0)):
            return False
        
        if not check(matrix(6,3)):
            return False
        
        if not check(matrix(6,6)):
            return False
        
        return True

        
        


