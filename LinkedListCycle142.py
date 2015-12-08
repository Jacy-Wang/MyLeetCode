# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p1 = head
        p2 = head
        sign = False
        while p1.next and p1.next.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                sign = True
                break
        if sign:
            p2 = head
            while p2 != p1:
                p2 = p2.next
                p1 = p1.next
            return p1
        return None
