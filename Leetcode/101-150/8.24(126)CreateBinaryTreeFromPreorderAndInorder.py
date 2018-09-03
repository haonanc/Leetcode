# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if preorder == [] or inorder == []:
            return None 
        root = TreeNode(preorder[0])
        recursion(preorder[1:],inorder,root)
        return root
        

def recursion(preord,inord,root):
    if len(inord) == 1:
        return
    v = root.val
    left = inord[:inord.index(v)]
    right = inord[inord.index(v)+1:]
    if len(left) != 0:
        root.left = TreeNode(preord[0])
        preord.pop(0)
        recursion(preord,left,root.left)
    if len(right) != 0:
        root.right = TreeNode(preord[0])
        preord.pop(0)
        recursion(preord,right,root.right)
        
    
