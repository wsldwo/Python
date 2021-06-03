# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    我想试试广度优先遍历 board priority search
    执行结果：通过
    执行用时：1008 ms, 在所有 Python3 提交中击败了7.76%的用户
    内存消耗：103.5 MB, 在所有 Python3 提交中击败了5.14%的用户
    慢的要死，哈哈
    '''
    def isSymmetric(self, root) -> bool:
        #对称检测
        def check(l):
            len_l = len(l)
            i,j = 0,len_l - 1
            while i <= j:
                if l[i] == l[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        if not root:
            return True
        else:
            con = [root]
            while len(con) > 0:
                temp_list = []
                temp_con = []
                for node in con:
                    temp_list.append(node.val if node else 'NULL')
                    temp_con.append(node.left if node else None)
                    temp_con.append(node.right if node else None)
                if check(temp_list):
                    if temp_con.count(None) == len(temp_con):
                        break
                    con.clear()
                    con += temp_con
                else:
                    return False
            return True
    '''
    突然发现，此题可用中序遍历搞定
    中序遍历的结果满足回文
    191 / 194 个通过测试用例
    最后执行的输入：[1,2,2,2,null,2]
    '''
    def isSymmetric(self, root) -> bool:
        #对称检测
        def check(l):
            len_l = len(l)
            i,j = 0,len_l - 1
            while i <= j:
                if l[i] == l[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        #中序遍历
        def inOrderTravesal(root):
            if root:
                inOrderTravesal(root.left)
                res.append(root.val)
                inOrderTravesal(root.right)
            else:
                #跳出循环,还是失败了
                '''
                i = 0
                len_res = len(res)
                while i < len_res:
                    a,b = i,i + 2 ** i
                    if b <= len_res:
                        should_return = True
                        for j in range(a,b):
                            if res[j] != 'Null':
                               should_return = False
                               break
                        if should_return:
                            return
                    i = b
                '''
                inOrderTravesal(None)
                res.append('Null')
                inOrderTravesal(None)
                
            
        res = []
        inOrderTravesal(root)
        return check(res)
    '''
    官方思路：别人的想法不得不服
    双指针，对称比较
    '''
    def isSymmetric(self, root) -> bool:
        def check(root1,root2):
            if not root1 and not root2:return True
            if not root1 or not root2:return False
            return root1.val == root2.val and check(root1.left,root2.right) and check(root1.right,root2.left)
        return check(root.left,root.right) if root else True

            
                


s = Solution()
s.isSymmetric(None)
