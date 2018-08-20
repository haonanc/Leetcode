# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        dict = {}
        if head == None:
            return None 
        temp = recursion(head,dict)
        return temp
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
def recursion(head,d):
    if head == None:
        return None
    if head not in d:
        temp = RandomListNode(head.label)
        d[head] = temp
        temp.next = recursion(head.next,d)
        temp.random = recursion(head.random,d)
        return temp   
    else:
        return d[head]
        
        
