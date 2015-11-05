class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        v = 1.0 * n
        while v > 1:
            v = v / 2
        if v == 1.0:
            return True
        return False
