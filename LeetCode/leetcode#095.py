# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left      
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        nums 剩余数字列表
        root 根节点
        node 当前节点
        '''
        def generate(nums,root,node):
            if root == None:
                for i in range(len(nums)):
                    #创建根节点
                    root = TreeNode(nums[i],None,None)
                    node = root
                    generate(nums[:i] + nums[i + 1:],root,node)
            else:
                left_nums,right_nums = [],[]
                for num in nums:
                    if num <= node.val:
                        left_nums.append(num)
                    else:
                        right_nums.append(num)
                #分配左节点
                for i in range(len(left_nums)):
                    left = TreeNode(nums[i],None,None)
                    node.left = left # 会被覆盖！！！
                    generate(left_nums[:i] + left_nums[i + 1:],root,left)
                #分配右节点
                for i in range(len(right_nums)):
                    right = TreeNode(nums[i],None,None)
                    node.right = right # 会被覆盖！！！
                    generate(right_nums[:i] + right_nums[i + 1:],root,right)
        def generate2(nums):
            for i in range(len(nums)):
                root = TreeNode(nums[i],None,None)
                pass
