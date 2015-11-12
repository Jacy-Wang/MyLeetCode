class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sLen = len(s)
        for i in xrange(sLen - 1, -1, -1):
            res += 26 ** (sLen- 1 - i) * (ord(s[i]) - 64)
        return res
