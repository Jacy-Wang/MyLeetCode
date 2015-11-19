class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowSign = False
        colSign = False
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        rowSign = True
                    if j == 0:
                        colSign = True
        for i in xrange(1, m):
            if matrix[i][0] == 0:
                matrix[i][1 :] = [0] * (n - 1)
        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0
        if colSign:
            for i in xrange(m):
                matrix[i][0] = 0
        if rowSign:
            matrix[0][:] = [0] * n
