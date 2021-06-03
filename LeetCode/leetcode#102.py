# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了52.91%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了45.24%的用户
    '''
    def levelOrder(self, root):
        if not root:
            return []
        else:
            res = [[root.val]]
            node_container = [] # 存放每一层节点的容器
            if root.left:
                node_container.append(root.left)
            if root.right:
                node_container.append(root.right)
            while len(node_container) > 0:
                r = [] # 中间结果
                temp = [] # 存储下一层节点
                for node in node_container:
                    r.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                res.append(r)
                node_container.clear()
                node_container += temp
        print(res)
        return res
