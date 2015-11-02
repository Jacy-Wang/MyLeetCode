# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        node = head
        newHead = None
        while node:
            nextNode = node.next
            if nextNode:
                node.next = nextNode.next
                nextNode.next = node
                if i != 0:
                    prevNode.next = nextNode
                elif i == 0:
                    newHead = nextNode
            elif i == 0:
                    newHead = node
            prevNode = node
            node = node.next
            i = i + 1
        return newHead
