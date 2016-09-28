class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = [1 for _ in xrange(n + 1)]
        for i in xrange(3, n + 1):
            for j in xrange(1, i / 2 + 1):
                val[i] = max(val[i], max(j, val[j]) * max(i - j, val[i - j]))
        return val[n]
