class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        maxRect = 0
        height = [0 for _ in xrange(len(matrix[0]))]
        left = [0 for _ in xrange(len(matrix[0]))]
        right = [len(matrix[0]) for _ in xrange(len(matrix[0]))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            leftMost = 0
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], leftMost)
                else:
                    leftMost = j + 1
                    left[j] = 0
            rightMost = len(matrix[0])
            for j in xrange(len(matrix[i]) - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(rightMost, right[j])
                else:
                    rightMost = j
                    right[j] = len(matrix[0])
            for j in xrange(len(matrix[i])):
                maxRect = max(maxRect, (right[j] - left[j]) * height[j])
        return maxRect
