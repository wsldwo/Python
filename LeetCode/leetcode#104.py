# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了77.87%的用户
    内存消耗：16.8 MB, 在所有 Python3 提交中击败了11.90%的用户
    '''
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = [0] # 用整形变量会存在未定义等问题，于是不得不用回列表
        def depth(root,cur_dep):# cur_dep 当前深度
            if not root: # 空节点
                max_depth[0] = cur_dep if cur_dep > max_depth[0] else max_depth[0]
            else:
                depth(root.left,cur_dep + 1)
                depth(root.right,cur_dep + 1)
        depth(root,0)
        return max_depth[0]
    
    '''
    进行简化
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了97.54%的用户
    内存消耗：16.9 MB, 在所有 Python3 提交中击败了5.10%的用户
    下次遇到通过递归求解一个整型值，是否也可以像这样不断生成结果，而不是依靠一个外部变量来存储？
    '''
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0
            else:
                return max(depth(root.left),depth(root.right)) + 1
        return 0 if not root else depth(root)

