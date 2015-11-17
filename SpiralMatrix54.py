class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        self.matrix = matrix
        self.res = []
        self.getOrder(len(matrix), len(matrix[0]), 0)
        return self.res
    
    def getOrder(self, m, n, k):
        if m >= 1 and n >= 1:
            for j in xrange(n):
                self.res.append(self.matrix[k][k + j])
            for i in xrange(1, m):
                self.res.append(self.matrix[k + i][k + j])
            if m >= 2 and n >= 2:
                for j in xrange(n - 2, -1, -1):
                    self.res.append(self.matrix[k + i][k + j])
                for i in xrange(m - 2, 0, -1):
                    self.res.append(self.matrix[k + i][k + j])
                self.getOrder(m - 2, n - 2, k + 1)
