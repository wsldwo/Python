'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def generateParenthesis(self, n):
        result = [] #结果集

        def dfs(left,right,res): #res为中间结果
            print(left,right,res)
            if left == 0 and right == 0: #左右括号都不剩余了，递归终止
                result.append(res)
                return
            if left > 0: #如果左括号还剩余的话，可以拼接左括号
                dfs(left - 1,right,res + '(')
                print('left-1')
            if right > left: #如果右括号剩余多于左括号剩余的话，可以拼接右括号
                dfs(left,right - 1,res + ')')
                print('right-1')

        dfs(n,n,'')

        return result

s = Solution()
print(s.generateParenthesis(3))