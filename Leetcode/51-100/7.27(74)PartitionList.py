# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        if head == None:
            return None
        h2 = None
        e2 = None
        cur = head
        toRet = None
        last = None
        while True:

            if cur.val < x:
                if toRet == None:
                    toRet = cur
                if last != None:
                    last.next = cur
                    last = None
                if cur.next != None:
                    if cur.next.val >= x:
                        last = cur
            else:
                if h2 == None:
                    h2 = cur
                    e2 = cur
                else:
                    e2.next = cur
                    e2 = cur 
                       
            if cur.next == None:
                break
            else:
                cur = cur.next
        
        if(last != None):        
            last.next = h2
        else:
            cur.next = h2 
        if e2 != None:
            e2.next = None 
        if toRet == None:
            return h2

        return toRet
                
            
        
        
        
        
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
