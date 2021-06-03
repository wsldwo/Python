'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
示例 1：
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:#修正除零错误
            print(s)
            return s
        strlen = len(s)
        res = []
        result = ''
        for x in range(numRows):
            res.append([])#初始化
        for i in range(strlen//(2*numRows-2)+1):
            j = i*(2*numRows-2)
            if j < strlen:#防止索引越界
                #放置竖列
                for k,v in enumerate(s[j:j+numRows]):
                    #print(k,v)
                    res[k].append(v)
                #放置斜列
                for k,v in enumerate(s[j+numRows:j+2*numRows-2]):
                    #print(numRows-k-2,v)
                    res[numRows-k-2].append(v)
        #print('#'.join(res))
        for x in res:
            result += ''.join(x)
        print(result)
        return result

s = Solution()
s.convert('A',1)