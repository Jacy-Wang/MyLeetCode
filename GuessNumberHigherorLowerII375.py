class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.table = [[0 for _ in xrange(n + 1)] for _ in xrange(n + 1)]
        self.MAX_INT = 2147483647
        return self.get(1, n)

    def get(self, left, right):
        if left >= right:
            return 0
        if self.table[left][right] != 0:
            return self.table[left][right]
        minVal = self.MAX_INT
        for i in xrange(left, right + 1):
            minVal = min(max(self.get(left, i - 1), self.get(i + 1, right)) + i, minVal)
        self.table[left][right] = minVal
        return minVal
