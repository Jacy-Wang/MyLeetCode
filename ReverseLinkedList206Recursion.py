# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(None, head)
    
    def reverse(self, head, newHead):
        if not newHead:
            return head
        else:
            nextHead = newHead.next
            newHead.next = head
            return self.reverse(newHead, nextHead)
