# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        node = head
        while node:
            if len(res) == 0:
                res.append(ListNode(node.val))
                curVal = node.val
            else:
                if node.val != curVal:
                    res.append(ListNode(node.val))
                    curVal = node.val
            node = node.next
        for i in xrange(len(res) - 1):
            res[i].next = res[i + 1]
        return res[0] if head else None
