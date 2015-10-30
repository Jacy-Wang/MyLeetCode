# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                res.append(ListNode(l1.val))
                l1 = l1.next
            else:
                res.append(ListNode(l2.val))
                l2 = l2.next
        if l1 != None:
            res.append(l1)
        elif l2 != None:
            res.append(l2)
        for i in xrange(len(res) - 1):
            res[i].next = res[i + 1]
        return res[0] if len(res) > 0 else None
