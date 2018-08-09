# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        toRet = [[]]
        cur = 1
        next = 0
        r = True
        queue = [root]
        while True:
            if cur == 0:
                if next == 0:
                    break
                toRet.append([])
                cur = next
                next = 0
                if r:
                    r = False
                else:
                    r = True

            temp = cur - 1
            toRet[-1].append(queue[temp].val)
            if r :
                if queue[temp].left != None:
                    queue.append(queue[temp].left)
                    next += 1
                if queue[temp].right != None:
                    queue.append(queue[temp].right)
                    next += 1
            else:
                if queue[temp].right != None:
                    queue.append(queue[temp].right)
                    next += 1
                if queue[temp].left != None:
                    queue.append(queue[temp].left)
                    next += 1
            del queue[temp]
            cur -= 1 
        return toRet 
