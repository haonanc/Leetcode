# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return recursion(root.left,root.right)
        """
        :type root: TreeNode
        :rtype: bool
        """
def recursion(node1,node2):
    if node1 == None and node2 == None:
        return True
    if node1 != None and node2 != None:
        if node1.val != node2.val:
            return False
        return recursion(node1.left,node2.right) and recursion(node1.right,node2.left)  
    return False
        
