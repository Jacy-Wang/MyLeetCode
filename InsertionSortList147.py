# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dum = ListNode(0)
        node = head.next
        head.next = None
        dum.next = head
        p = dum
        while node:
            nextNode = node.next
            if node.val < p.next.val:
                p = dum
            while p.next and p.next.val <= node.val:
                p = p.next
            node.next = p.next
            p.next = node
            node = nextNode
        return dum.next
