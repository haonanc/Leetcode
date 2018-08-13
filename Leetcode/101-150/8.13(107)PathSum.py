# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        if root == None:
            return []
        toRet = []
        list = []
        recursion(root,sum,list,toRet)
        return toRet
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
def recursion(node,target,list,toRet):
    v = node.val
    list.append(v)
    bl = (node.left == None)
    br = (node.right == None)
    if target - v == 0 and bl and br:
        toRet.append(copy.deepcopy(list))
        list.pop()
        return
    if not bl:
        recursion(node.left,target-v,list,toRet)      
    if not br:
        recursion(node.right,target-v,list,toRet)  
    list.pop()
    
    
        
