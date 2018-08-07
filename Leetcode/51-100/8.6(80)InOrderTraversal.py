# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        toRet = []
        recursion(root,toRet)
        return toRet
def recursion(root,toRet):
    if root.left != None:
        recursion(root.left,toRet)
    toRet.append(root.val)
    if root.right != None:
        recursion(root.right,toRet)
    
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
