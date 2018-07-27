# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        if(root == None):
            return True
        list = []
        recursion(root,list)
        print(list)
        if len(list) != len(set(list)):
            return False
        if(sorted(list) == list):
            return True
        return False
        """
        :type root: TreeNode
        :rtype: bool
        """

def recursion(node,list):
    if(node.left != None):
        recursion(node.left,list)
    list.append(node.val)
    if(node.right != None):
        recursion(node.right,list)
        
        
