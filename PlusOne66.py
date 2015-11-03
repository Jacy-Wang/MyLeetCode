class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sign = False
        for i in xrange(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                sign = False
                digits[i] = digits[i] + 1
                break
            else:
                sign = True
                digits[i] = 0
        return [1] + digits if sign else digits
