class Solution:
    '''
    忽略了将当前节点与父节点的父节点进行比较，失败一次
    执行结果：通过
    执行用时：124 ms, 在所有 Python3 提交中击败了8.11%的用户
    内存消耗：17.3 MB, 在所有 Python3 提交中击败了40.31%的用户
    差点超时，代码丑得不行，哈哈哈
    '''
    def isValidBST(self, root):
        if not root: # 空树是特殊的二叉搜索树
            return True
        else:
            if root.left:
                if root.left.val >= root.val:
                    return False
                '''
                修正：检测所有左子树是否都严格小于根节点
                '''
                con = []
                if root.left.left:
                    con.append(root.left.left)
                if root.left.right:
                    con.append(root.left.right)
                while len(con) > 0:
                    temp = []
                    for node in con:
                        if node.val >= root.val:
                            return False
                        if node.left:
                            temp.append(node.left)
                        if node.right:
                            temp.append(node.right)
                    con.clear()
                    con += temp
                
            if root.right:
                if root.right.val <= root.val:
                    return False
                '''
                修正：检测所有子右树是否都严格大于根节点
                '''
                con = []
                if root.right.left:
                    con.append(root.right.left)
                if root.right.right:
                    con.append(root.right.right)
                while len(con) > 0:
                    temp = []
                    for node in con:
                        if node.val <= root.val:
                            return False
                        if node.left:
                            temp.append(node.left)
                        if node.right:
                            temp.append(node.right)
                    con.clear()
                    con += temp
            
            left_value =  self.isValidBST(root.left)
            right_value = self.isValidBST(root.right)
            if left_value and right_value:
                return True
            else:
                return False
            
    '''
    参考答案
    不得不服，人家的思路
    二叉搜索树的每一个节点值，都有上下界
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):# 右子树改下界
                return False
            if not helper(node.left, lower, val):#  左子树改上界
                return False
            return True

        return helper(root)

