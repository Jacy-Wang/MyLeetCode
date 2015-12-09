# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        return self.mergeSort(head, length)
    
    def mergeSort(self, head, length):
        if length == 0 or length == 1:
            return head
        else:
            head1 = head
            p = head
            for i in xrange(length / 2 - 1):
                p = p.next
            head2 = p.next
            p.next = None
            newHead1 = self.mergeSort(head1, length / 2)
            newHead2 = self.mergeSort(head2, length - length / 2)
            return self.merge(newHead1, newHead2)

    def merge(self, head1, head2):
        dum = ListNode(0)
        curNode = dum
        while head1 and head2:
            if head1.val < head2.val:
                curNode.next = ListNode(head1.val)
                head1 = head1.next
            else:
                curNode.next = ListNode(head2.val)
                head2 = head2.next
            curNode = curNode.next
        if head1:
            curNode.next = head1
        if head2:
            curNode.next = head2
        return dum.next
