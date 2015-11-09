# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        mid = head
        end = head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        if end.next:
            end = end.next
        secHalfNext = mid.next
        mid.next = end
        while secHalfNext != end:
            secHalf = secHalfNext
            endNext = end.next
            end.next = secHalf
            secHalfNext = secHalf.next
            secHalf.next = endNext
        left = head
        right = end
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
