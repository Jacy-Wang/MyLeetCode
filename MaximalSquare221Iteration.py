class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.matrix = matrix
        square = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '1':
                    r = i + 1
                    c = j + 1
                    while r < len(matrix) and c < len(matrix[0]):
                        if matrix[r][c] == '1':
                            if not self.check(i, r, j, c):
                                break
                            else:
                                r += 1
                                c += 1
                        else:
                            break
                    square = max(square, (r - i) ** 2)
        return square

    def check(self, rowStart, rowEnd, colStart, colEnd):
        for i in xrange(rowStart, rowEnd):
            if self.matrix[i][colEnd] != '1':
                return False
        for j in xrange(colStart, colEnd):
            if self.matrix[rowEnd][j] != '1':
                    return False
        return True
