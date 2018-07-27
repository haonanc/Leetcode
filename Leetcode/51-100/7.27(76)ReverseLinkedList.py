class Solution:
    def reverseBetween(self, head, m, n):
        if(m == n):
            return head 
        counter = 1
        pre = ListNode(0) 
        pre.next = head
        cur = head
        head = pre
        storepre = None
        storecur = None
        while(True):
            if counter < m:
                counter += 1
                pre = cur
                cur = cur.next      
            elif counter == m:
                storepre = pre
                storecur = cur
                counter += 1
                pre = cur
                cur = cur.next
            elif counter > m and counter < n:
                counter += 1
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            elif counter == n:
                storepre.next = cur
                storecur.next = cur.next
                cur.next = pre
                break

        return head.next
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
