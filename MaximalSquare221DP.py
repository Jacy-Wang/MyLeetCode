class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        res = 0
        Max = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                Max[i][j] = int(matrix[i][j])
                if i > 0 and j > 0 and Max[i][j]:
                    Max[i][j] = min(Max[i - 1][j - 1], Max[i - 1][j], Max[i][j - 1]) + 1
                res = max(res, Max[i][j])
        return res ** 2
