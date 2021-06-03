# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    本题采用前序、中序、后序遍历皆可
    执行结果：通过
    执行用时：36 ms, 在所有 Python3 提交中击败了84.08%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了9.59%的用户
    '''
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrderTraversal(node1,node2):
            if node1 and node2:
                if node1.val == node2.val:
                    if not preOrderTraversal(node1.left,node2.left):
                        return False
                    if not preOrderTraversal(node1.right,node2.right):
                        return False
                    return True
                else:
                    return False
            elif not node1 and not node2:
                return True
            else:
                return False
        return preOrderTraversal(p,q)
        