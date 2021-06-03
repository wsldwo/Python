class Solution:
    '''
    执行结果：通过
    执行用时：60 ms, 在所有 Python3 提交中击败了71.54%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了80.12%的用户
    '''
    def totalNQueens(self, n):
        def dfs(n,rows,columns,diagonals1,diagonals2,path,res):
            #print(f'rows:{rows} columns:{columns} dia1:{diagonals1} dia2:{diagonals2} path:{path}')
            if rows >= n:#到n - 1就下完了
                '''
                在回溯算法中，只有结果集变量可以写在代码块中进行添加修改，其余存储中间结果的变量统统都要放入dfs函数的形参列表中进行修改
                '''
                res.append(path)
                #print(path)
                return
            for i in range(n):
                #此时的行列坐标是（rows,i）
                '''
                columns:列下标容器
                diagonals1：斜线1容器，特征为 “行-列”值不变
                diagonals2：斜线2容器，特征为 “行+列”值不变
                '''
                if i not in columns and rows - i not in diagonals1 and rows + i not in diagonals2:
                    #columns.append(i) 错误，只有结果集变量可以写在代码块中进行添加修改
                    #diagonals1.append(rows - i) 错误，只有结果集变量可以写在代码块中进行添加修改
                    #diagonals2.append(rows + i) 错误，只有结果集变量可以写在代码块中进行添加修改
                    #path.append((rows,i)) 错误，只有结果集变量可以写在代码块中进行添加修改
                    #print(path) 错误，只有结果集变量可以写在代码块中进行添加修改
                    '''
                    在回溯算法中，只有结果集变量可以写在代码块中进行添加修改，其余存储中间结果的变量统统都要放入dfs函数的形参列表中进行修改
                    '''
                    dfs(n,rows + 1,columns + [i],diagonals1 + [rows - i],diagonals2 + [rows + i],path + [(rows,i)],res)
        res = []
        dfs(n,0,[],[],[],[],res)
        print(res)
        def translate(res):
            r = []
            for x in res:
                l = list('.'*(n - 1))#修正'.'的数量
                l.insert(x[1],'Q')
                r.append(''.join(l))
            return r
        result = []
        for i in range(len(res)):
            result.append(translate(res[i]))
        print(result)
        return len(result)

s = Solution()
print(s.totalNQueens(5))