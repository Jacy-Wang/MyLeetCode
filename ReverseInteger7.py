class Solution(object):
    maxint = 2147483647
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            end = 0
            res = ''
        else:
            end = 1
            res = '-'
        strX = str(x)
        i = len(strX) - 1
        while i >= end:
            res = res + strX[i]
            i = i - 1
        return int(res) if -(self.maxint + 1) <= int(res) <= self.maxint else 0
