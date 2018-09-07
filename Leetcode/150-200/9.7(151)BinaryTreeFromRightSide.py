# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        ans = []
        preOrder(root,ans,1)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """
def preOrder(node,ans,height):
    if node == None:
        return 
    if height > len(ans):
        ans.append(node.val)
    preOrder(node.right,ans,height+1)
    preOrder(node.left,ans,height+1)
