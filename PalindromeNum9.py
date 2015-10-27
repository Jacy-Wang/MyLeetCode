class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            digits = 1
            while x / 10 ** digits >= 1:
                digits = digits + 1
            for i in xrange(digits / 2):
                if x % 10 != x / 10 ** (digits - 2 * i - 1):
                    return False
                x = x % 10 ** (digits - 2 * i - 1)
                x = x / 10
            return True
