class Solution:
    '''
    执行结果：通过
    执行用时：3588 ms, 在所有 Python3 提交中击败了28.08%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了70.66%的用户
    回溯大法好！！！
    '''
    def exist(self, board, word):
        m = len(board) # 行数
        n = len(board[0]) # 列数
        def travel(board,x,y,word,index,path,res):
            if index == len(word):
                res.append(path)
                return
            # x,y为当前坐标
            possible_path = []
            # 上方
            if x - 1 >= 0 and (x - 1,y) not in path:
                if board[x - 1][y] == word[index]:
                    possible_path.append((x - 1,y))
                    #travel(board,x - 1,y,word,index + 1,path + [(x - 1,y)],res)
                    #return
            # 下方
            if x + 1 <= m - 1 and (x + 1,y) not in path:
                if board[x + 1][y] == word[index]:
                    possible_path.append((x + 1,y))
                    #travel(board,x + 1,y,word,index + 1,path + [(x + 1,y)],res)
                    #return
            # 左边
            if y - 1 >= 0 and (x,y - 1) not in path:
                if board[x][y - 1] == word[index]:
                    possible_path.append((x,y - 1))
                    #travel(board,x,y - 1,word,index + 1,path + [(x,y - 1)],res)
                    #return
            # 右边
            if y + 1 <= n - 1 and (x,y + 1) not in path:
                if board[x][y + 1] == word[index]:
                    possible_path.append((x,y + 1))
                    #travel(board,x,y + 1,word,index + 1,path + [(x,y + 1)],res)
                    #return            
            for x1,y1 in possible_path:
                travel(board,x1,y1,word,index + 1,path + [(x1,y1)],res)
        res = []
        #首先找到首字母的所有坐标
        first_pos = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    first_pos.append((i,j))
        for x,y in first_pos:
            travel(board,x,y,word,1,[(x,y)],res)
        print(res)
        if len(res) > 0:
            return True
        else:
            return False
s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
