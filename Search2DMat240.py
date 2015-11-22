class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowLen = len(matrix)
        colIdx= len(matrix[0]) - 1
        for i in xrange(rowLen):
            for j in xrange(colIdx, -1, -1):
                if matrix[i][j] <= target:
                    break
                else:
                    colIdx -= 1
            if matrix[i][j] == target:
                return True
        return False
