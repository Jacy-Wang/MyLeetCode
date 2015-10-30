# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curNode = head
        counter = 0
        pos = head
        while curNode != None:
            counter = counter + 1
            curNode = curNode.next
            if counter == n and not curNode:
                return head.next
            elif counter >= n + 2:
                pos = pos.next
        pos.next = pos.next.next
        return head
