# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        if check(root) == -1:
            return False
        return True
        
        """
        :type root: TreeNode
        :rtype: bool
        """
def check(node):
    if node == None:
        return 0
    l = check(node.left)
    r = check(node.right)
    if l == -1 or r == -1 or abs(l-r) > 1:
        return -1
    return 1 + max(l,r)
    
