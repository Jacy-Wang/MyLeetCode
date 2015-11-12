class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = bin(n)[2 :]
        binN = "0" * (32 - len(tmp)) + tmp
        return int(binN[: : -1], 2)
