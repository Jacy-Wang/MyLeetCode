class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        dist = 1
        while dist * 2 <= n:
            first += dist
            dist *= 2
            if dist * 2 > n:
                return first
            if (n / dist) % 2 == 1:
                first += dist
            dist *= 2
        return first
