class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        nums = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    nums[i][j] = 1
                elif i > 0 and j > 0:
                    nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
        return nums[m - 1][n - 1]
