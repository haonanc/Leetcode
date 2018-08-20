# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(-2*31)
        dummy.next = head 
        recursion(dummy,head)
        return dummy.next 
def recursion(pre,cur):
    if cur == None:
        return 
    if pre.val == cur.val:
        pre.val = "@"
        recursion(cur,cur.next)
        cur.val = "@"
    else:
        recursion(cur,cur.next)
        if pre.val != "@" and cur.val == "@":
            cur = cur.next
            while cur != None:
                if cur.val != "@":
                    break
                cur = cur.next
            pre.next = cur
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
