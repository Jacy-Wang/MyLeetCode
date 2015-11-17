# a note: recursion would exceeds time limit for this problem
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        nums = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
        return nums[m - 1][n - 1]
