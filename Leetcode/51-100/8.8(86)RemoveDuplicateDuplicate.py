# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        v = -2**31
        pre = None
        cur = head
        bo = False
        while cur.next != None:
            if cur.val == v:
                cur = cur.next
                bo = True
            else:
                v = cur.val
                if bo:
                    pre.next = cur
                    pre = None
                    bo = False
                pre = cur
                cur = cur.next
        if cur.val == v:
            pre.next = None
        else:
            pre.next = cur
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
