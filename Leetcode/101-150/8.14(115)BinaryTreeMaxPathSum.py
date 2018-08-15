# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        if root == None:
            return 0
        m = [-2**31]
        ro = getMax(root,m)
        return max(m[0],ro)
        """
        :type root: TreeNode
        :rtype: int
        """
def getMax(root,m):
    r,l = 0,0
    if root.left != None:
        l = getMax(root.left,m)
    if root.right != None:
        r = getMax(root.right,m)
    single = root.val + max(l,r,0)
    m[0] = max(m[0],root.val+l+r,single)      
    return single
