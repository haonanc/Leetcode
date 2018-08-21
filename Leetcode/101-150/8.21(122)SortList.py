# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        while head != None:
            count += 1
            head = head.next
        index = 1
        while index < count:
            mergeHelper(dummy,dummy.next,index)
            index *= 2
        return dummy.next
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
def mergeHelper(pre,head,count):
    pre.next = head
    l1 = head
    cur = head
    counter = count
    if cur == None:
        return
    while counter > 1:
        if cur == None:
            return
        cur = cur.next
        counter -= 1
    if cur == None:
        return
    counter = count
    temp = cur
    cur = cur.next
    if cur == None:
        return
    temp.next = None
    l2 = cur
    while counter > 1:
        cur = cur.next
        counter -= 1
        if cur == None:
            a,b = merge(l1,l2)
            pre.next = a
            return
    temp = cur
    cur = cur.next
    temp.next = None 
    
    a,b = merge(l1,l2)
    pre.next = a
    mergeHelper(b,cur,count)
    

def merge(l1,l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 != None and l2 != None:
        if l1.val > l2.val:
            cur.next = l2
            cur = l2
            l2 = l2.next
        else:
            cur.next = l1
            cur = l1
            l1 = l1.next
    if l1 == None:
        cur.next = l2
        end = l2
    else:
        cur.next = l1
        end = l1
    while end.next != None:
        end = end.next
    return dummy.next,end
        
            
