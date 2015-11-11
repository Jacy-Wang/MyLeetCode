# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        lst = []
        while head:
            if head.val != val:
                lst.append(ListNode(head.val))
            head = head.next
        if not lst:
            return lst
        for i in xrange(len(lst) - 1):
            lst[i].next = lst[i + 1]
        return lst[0]
