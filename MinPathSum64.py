class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        top = [0 for _ in xrange(n)]
        bottom = [0 for _ in xrange(n)] 
        top[0] = grid[0][0]
        for j in xrange (1, n):
            top[j] = top[j - 1] + grid[0][j]
        for i in xrange(1, m):
            for j in xrange(n):
                if j == 0:
                    bottom[j] = top[j] + grid[i][j]
                else:
                    bottom[j] = min(top[j], bottom[j - 1]) + grid[i][j]
            top = bottom
        return top[n - 1]
