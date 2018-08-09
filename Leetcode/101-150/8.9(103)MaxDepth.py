# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        return recursion(0,root)
        """
        :type root: TreeNode
        :rtype: int
        """
def recursion(depth,node):
    if node == None:
        return depth
    return max(recursion(depth+1,node.left),recursion(depth+1,node.right))
        
