# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if postorder == [] or inorder == []:
            return None 
        root = TreeNode(postorder[-1])
        recursion(postorder[:-1],inorder,root)
        return root
        

def recursion(postord,inord,root):
    if len(inord) == 1:
        return
    v = root.val
    left = inord[:inord.index(v)]
    right = inord[inord.index(v)+1:]
    if len(right) != 0:
        root.right = TreeNode(postord[-1])
        postord.pop()
        recursion(postord,right,root.right)
    if len(left) != 0:
        root.left = TreeNode(postord[-1])
        postord.pop()
        recursion(postord,left,root.left)   
