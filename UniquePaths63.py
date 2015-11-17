class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rowLen = len(obstacleGrid)
        colLen = len(obstacleGrid[0])
        nums = [[0 for _ in xrange(colLen)] for _ in xrange(rowLen)]
        rowSign = False
        colSign = False
        for i in xrange(rowLen):
            for j in xrange(colLen):
                if obstacleGrid[i][j] == 1:
                    nums[i][j] = 0
                    if i == 0:
                        colSign = True
                    if j == 0:
                        rowSign = True
                else:
                    if i == 0:
                        if not colSign:
                            nums[i][j] = 1
                    if j == 0:
                        if not rowSign:
                            nums[i][j] = 1
                    if i > 0 and j > 0:
                        nums[i][j] = nums[i - 1][j] + nums[i][j - 1]
        return nums[rowLen - 1][colLen - 1]
