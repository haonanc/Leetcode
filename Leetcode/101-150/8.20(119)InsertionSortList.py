# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head == None:
            return None
        begin = ListNode("b")
        end = ListNode("e")
        begin.next = end
        end.next = head 
        largest = ListNode(-2**31)
        while end.next != None:
            catch = end.next
            end.next = end.next.next
            find = begin
            if catch.val >= largest.val:
                largest = catch   
            while find.next.val != "e":
                if catch.val < find.next.val:
                    break
                find = find.next
            catch.next = find.next
            find.next = catch    
        largest.next = None 
        return begin.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
