class Solution:
    '''
    自己写的大数乘法！！！
    执行结果：通过
    执行用时：408 ms, 在所有 Python3 提交中击败了7.45%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.55%的用户
    '''
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = []
        len1 = len(num1)
        len2 = len(num2)
        num1_list = list(num1)
        num1_list.reverse()
        num2_list = list(num2)
        num2_list.reverse()
        
        #print(num1_list)
        #print(num2_list)
        
        for i in range(len1):
            num = '' + '0' * i #中间结果
            increase = 0 #进位值
            for j in range(len2):
                r = int(num1_list[i]) * int(num2_list[j]) + increase
                print(r)
                if r >= 10:
                    num += str(r % 10)
                    increase = r // 10
                else:
                    num += str(r)
                    increase = 0
                
                if j == len2 - 1 and increase != 0:#进位修正
                    num += str(increase)
                
            res.append(num)

        print(res)

        def add(n1,n2):
            n1_list = list(n1)
            n2_list = list(n2)

            n1_len = len(n1)
            n2_len = len(n2)

            incre = 0
            nu = ''

            length = max([n1_len,n2_len])

            for i in range(length):
                a = None
                b = None

                if i >= n1_len:
                    a = '0'
                else:
                    a = n1_list[i]

                if i >= n2_len:
                    b = '0'
                else:
                    b = n2_list[i]


                re = int(a) + int(b) + incre

                if re >= 10:
                    nu += str(re % 10)
                    incre = re // 10
                else:
                    nu += str(re)
                    incre = 0
                
                if i == length - 1 and incre != 0:#进位修正
                    nu += str(incre)
            
            return nu
        
        result = '0'
        for i in range(len(res)):
            result  = add(result,res[i])
        
        print(''.join(reversed(list(result))))
        return ''.join(reversed(list(result)))

    '''
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了90.73%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了55.43%的用户
    '''
    def multiply2(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))




s = Solution()
s.multiply('123','456')
s.multiply('456','123')
        

