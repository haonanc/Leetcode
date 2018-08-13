# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        return check(root) + 1

        """
        :type root: TreeNode
        :rtype: int
        """
def check(root):
    if root.left != None and root.right != None:
        return min(check(root.right),check(root.left)) + 1
    elif root.left != None:
        return check(root.left) + 1
    elif root.right != None:
        return check(root.right) + 1
    else:
        return 0
       
