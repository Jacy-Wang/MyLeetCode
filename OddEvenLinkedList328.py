# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head2 = head.next
        p1 = head
        p2 = head2
        node = head2.next
        counter = 0
        while node:
            counter += 1
            if counter & 1 != 0:
                p1.next = node
                p1 = p1.next
            else:
                p2.next = node
                p2 = p2.next
            node = node.next
        p2.next = None
        p1.next = head2
        return head
