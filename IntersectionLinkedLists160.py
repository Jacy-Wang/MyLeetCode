# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            if headA == headB:
                return headA
            endA = headA
            while endA and endA.next:
                endA = endA.next
            node = headB
            lenB = 0
            while node:
                lenB += 1
                node = node.next
            endA.next = headB
            p1 = headA
            for _ in xrange(lenB):
                p1 = p1.next
            p2 = headA
            while p1:
                if p2 == p1:
                    endA.next = None
                    return p2
                p1 = p1.next
                p2 = p2.next
            endA.next = None
