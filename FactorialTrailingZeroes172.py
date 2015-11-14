class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        while n >= 5:
            counter += (n / 5)
            n /= 5
        return counter
