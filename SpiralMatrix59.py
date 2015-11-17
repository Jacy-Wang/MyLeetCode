class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        self.res = [[0 for _ in xrange(n)] for _ in xrange(n)]
        self.getSquare(n, 0, 1)
        return self.res

    def getSquare(self, n, k, start):
        if n >= 1:
            for j in xrange(n):
                self.res[k][k + j] = start + j
            for i in xrange(k + 1, n):
                self.res[k + i][j] = start + n + i - 1 
            for j in xrange(n - 2, -1, -1):
                self.res[i][k + j] = start + 3 * n - j - 3 
            for i in xrange(n - 2, 0, -1):
                self.res[k + i][j] = start + 4 * n - i - 4
            self.getSquare(n - 2, k + 1, start + 4 * n - 4)
