# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        # return reverseRecursion(None,head)
        return reverseIterative(head)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
def reverseRecursion(pre,node):
    if node == None:
        return pre
    temp = node.next
    node.next = pre
    return reverseRecursion(node,temp)

def reverseIterative(head):
    pre = None
    node = head
    while node:
        temp = node.next
        node.next = pre
        pre = node 
        node = temp
 
    return pre
