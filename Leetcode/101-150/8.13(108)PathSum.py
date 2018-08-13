# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, target):
        if root == None:
            return False
        v = root.val
        if root.left == None and root.right == None:
            return (v == target)
        else:
            return self.hasPathSum(root.left,target - v) or self.hasPathSum(root.right,target - v)
