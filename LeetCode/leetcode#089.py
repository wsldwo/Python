class Solution:
    '''
    回溯可以做，但是当n>=10时，超出递归深度了。
    '''
    def grayCode(self, n):
        if n == 0:
            print([0])
            return [0]
        def binToDem(s):#二进制转十进制
            r = 0
            len_s = len(s)
            for i in range(len_s):
                r += int(s[i]) * 2 ** (len_s - i - 1)
            return r
        '''
        这是我一直以来所坚持的回溯写法
        path存储中间结果，只能在形参列表修改
        res存储最终结果，只能在代码块修改
        '''
        def dfs(num,length,path,res):
            if len(res) == 1: #本题只用找到1个答案
                return
            if length == 0:
                res.append(path)
                return
            for i in range(len(num)):
                if num[i] == '1':
                    temp = num[:i] + '0' + num[i + 1:]
                    if temp not in path:
                        dfs(temp,length - 1,path + [temp],res)
                else:
                    temp = num[:i] + '1' + num[i + 1:]
                    if temp not in path:
                        dfs(temp,length - 1,path + [temp],res)
        '''
        上边的回溯不是不行，而是搜索所有解会超时，此题只需要找出一种解即可，故消去结果集变量res
        不行！！！
        这种写法还是有问题！！！别人的招还是没学会！！！
        
        path = ['0' * n]
        def dfs2(num,length,res):
            if len(res) == length:
                return res
            for i in range(len(num)):
                    temp = num[:i] + str(int(num[i]) ^ 1) + num[i + 1:]
                    if temp not in path:
                        path.append(temp)
                        res.append(temp)
                        if dfs2(temp,length,res):
                            return res
                        path.pop()
                        res.pop()
        res = dfs2('0' * n,2 ** n,['0' * n])
        '''
        res = []
        dfs('0' * n,2 ** n - 1,['0' * n],res)
        print(res)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = binToDem(res[i][j])
        print(res)
        return res
    '''
    答案1
    先求解n==i的解，再求解n==i+1的解
    在之前的解前边加上0和1，然后对称复制低位（最后一个复制第一个的低位，倒数第二个复制第二个低位）
    如果知道了 n = 2 的解的话，如果是 { 0, 1, 3, 2}，那么 n = 3 的解就是 { 0, 1, 3, 2, 2 + 4, 3 + 4, 1 + 4, 0 + 4 }，
    即 { 0 1 3 2 6 7 5 4 }。之前的解直接照搬过来，然后倒序把每个数加上 1 << ( n - 1) 添加到结果中即可。
    '''
    def grayCode2(self, n):
        res = [0]
        for i in range(1,n + 1):
            copy = list(reversed(res.copy()))
            for j in range(len(copy)):
                res.append(copy[j] + 2 ** (i - 1))
        return res
    '''
    答案2
    格雷码公式：i ^ i/2 即i ^ (i >> 1)
    '''
    def grayCode3(self, n):
        res = []
        length = 1 << n # 等价于 2^n   左移乘二  右移除二
        for i in range(length):
            res.append(i ^ i >> 1)
        return res

s = Solution()
s.grayCode(4)
