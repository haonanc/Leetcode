# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []
        toRet = [[]]
        cur = 1
        next = 0
        queue = [root]
        while True:
            if cur == 0:
                if next == 0:
                    break
                toRet.append([])
                cur = next
                next = 0           
            toRet[-1].append(queue[0].val)
            if queue[0].left != None:
                queue.append(queue[0].left)
                next += 1
            if queue[0].right != None:
                queue.append(queue[0].right)
                next += 1
            del queue[0]
            cur -= 1 
        return toRet 
            
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
