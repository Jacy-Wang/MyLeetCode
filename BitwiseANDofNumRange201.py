class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bits = 0
        while m != n:
            m >>= 1
            n >>= 1
            bits += 1
        return m << bits
