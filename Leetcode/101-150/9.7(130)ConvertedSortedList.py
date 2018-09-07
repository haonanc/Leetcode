# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, start):
        if start == None:
            return None
        if start.next == None:
            return TreeNode(start.val)

        slow,fast = start,start
        while fast:
            if fast.next == None:
                break
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        cur = TreeNode(slow.val)
        cur.left = self.sortedListToBST(start)
        cur.right = self.sortedListToBST(slow.next)

        return cur
