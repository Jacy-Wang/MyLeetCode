class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        num = [1 for _ in xrange(n + 1)]
        num[1] = 10
        for i in xrange(2, n + 1):
            for j in xrange(9, 10 - i, -1):
                num[i] *= j
            num[i] *= 9
        return sum([num[j] for j in xrange(1, n + 1)])
