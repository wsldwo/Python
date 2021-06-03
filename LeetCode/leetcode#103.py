# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    执行用时：32 ms, 在所有 Python3 提交中击败了96.30%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了53.01%的用户
    跟上题差不多
    '''
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        else:
            res = [[root.val]]
            node_container = [] # 存放每一层节点的容器
            if root.left:
                node_container.append(root.left)
            if root.right:
                node_container.append(root.right)
            rtol = True # 右到左
            while len(node_container) > 0:
                r = [] # 中间结果
                temp = [] # 存储下一层节点
                if rtol:
                    for node in reversed(node_container):
                        r.append(node.val)
                else:
                    for node in node_container:
                        r.append(node.val)
                
                for node in node_container:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                res.append(r)
                node_container.clear()
                node_container += temp
                rtol = not rtol
        print(res)
        return res
