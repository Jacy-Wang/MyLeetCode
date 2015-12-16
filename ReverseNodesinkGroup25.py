# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or k == 1 or not head:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        dum = ListNode(0)
        node = head
        i = 0
        nextHead = dum
        while node and i < (length / k) * k:
            i += 1
            if i % k == 1:
                curHead = nextHead
                nextHead = node
            nextNode = node.next
            node.next = curHead.next
            curHead.next = node
            node = nextNode
        nextHead.next = node
        return dum.next
