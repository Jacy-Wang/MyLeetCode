class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        digits = []
        extraDigit = 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                raw = l1.val + l2.val + extraDigit
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                raw = l1.val + extraDigit
                l1 = l1.next

            else:
                raw = l2.val + extraDigit
                l2 = l2.next
            curDigit, extraDigit = self.getCurDigit(raw)
            digits.append(ListNode(curDigit))
        
        if extraDigit > 0:
            digits.append(ListNode(extraDigit))
        for i in xrange(len(digits) - 1):
            digits[i].next = digits[i + 1]
        return digits[0]

    def getCurDigit(self, curSum):
        return curSum % 10, curSum / 10
