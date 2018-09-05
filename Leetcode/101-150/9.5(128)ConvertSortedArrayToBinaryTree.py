# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None
        node = TreeNode(nums[len(nums)/2])
        recursion(node,nums)
        return node
        
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
def recursion(node,l):   
    m = int(len(l)/2)

    if m != 0:
        ll = l[:m]
        node.left = TreeNode(ll[len(ll)/2])  
        recursion(node.left,ll)
    if m < len(l) - 1:
        lr = l[m+1:]
        node.right = TreeNode(lr[len(lr)/2]) 
        recursion(node.right,lr)
    
