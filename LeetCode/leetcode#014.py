'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs_len = len(strs)
        if strs_len == 0:
            return ''
        if strs_len == 1:
            return strs[0]
        if '' in strs:
            return ''
        mcp = ''
        for k,v in enumerate(strs[0]):
            mcp += v
            for w,x in enumerate(strs[1:]):
                if x.startswith(mcp):
                    continue
                else:
                    print(mcp[:-1])
                    return mcp[:-1]
            if k == len(strs[0]) - 1:#切记不能忘记处理达到末尾时的特殊情况
                print(strs[0])
                return strs[0]
s = Solution()
s.longestCommonPrefix(["flower","flower","flow","flower"])